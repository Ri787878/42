# include "../codexion.h"

# include <errno.h>

static void	stop_locked(struct codexion_struct *cdx)
{
	cdx->stop_requested = true;
	pthread_cond_broadcast(&cdx->coordinator_changed);
}

static t_coder	*next_waiting_coder(struct codexion_struct *cdx)
{
	t_coder	*best;
	t_coder	*candidate;
	int		i;

	best = NULL;
	i = 0;
	while (i < cdx->config.nb_coders)
	{
		candidate = &cdx->coders[i];
		if (candidate->state == WAITING)
		{
			if (best == NULL
				|| (cdx->config.scheduler == FIFO
					&& candidate->request_sequence < best->request_sequence)
				|| (cdx->config.scheduler == EDF
					&& (candidate->tm_lst_compile < best->tm_lst_compile
						|| (candidate->tm_lst_compile == best->tm_lst_compile
							&& candidate->request_sequence
							< best->request_sequence))))
				best = candidate;
		}
		i++;
	}
	return (best);
}

static int	dongles_ready(t_coder *coder, int64_t elapsed)
{
	if (coder->left_dongle == coder->right_dongle)
		return (0);
	if (coder->left_dongle->in_use || coder->right_dongle->in_use)
		return (0);
	return (coder->left_dongle->available_at_ms <= elapsed
		&& coder->right_dongle->available_at_ms <= elapsed);
}

static int	acquire_dongles(t_coder *coder)
{
	struct codexion_struct	*cdx;
	struct timespec			deadline;
	t_coder					*next;
	int64_t					elapsed;
	int64_t					ready_at;
	int						result;
	long					wait_ms;

	cdx = coder->cdx;
	result = pthread_mutex_lock(&cdx->coordinator_mutex);
	if (result != 0)
	{
		fprintf(stderr, "coder %d: failed to lock coordinator\n", coder->id);
		return (0);
	}
	coder->request_sequence = ++cdx->next_request_sequence;
	coder->state = WAITING;
	while (!cdx->stop_requested)
	{
		next = next_waiting_coder(cdx);
		elapsed = get_time_elapsed_ms(cdx);
		if (elapsed < 0)
		{
			fprintf(stderr, "coder %d: failed to read elapsed time\n",
				coder->id);
			stop_locked(cdx);
			break ;
		}
		if (next == coder && dongles_ready(coder, elapsed))
		{
			coder->left_dongle->in_use = true;
			coder->right_dongle->in_use = true;
			coder->tm_lst_compile = elapsed;
			coder->state = COMPILING;
			log_event_locked(cdx, coder->id, "has taken a dongle");
			log_event_locked(cdx, coder->id, "has taken a dongle");
			log_event_locked(cdx, coder->id, "is compiling");
			pthread_mutex_unlock(&cdx->coordinator_mutex);
			return (1);
		}
		if (next == coder && coder->left_dongle != coder->right_dongle
			&& !coder->left_dongle->in_use && !coder->right_dongle->in_use)
		{
			ready_at = coder->left_dongle->available_at_ms;
			if (coder->right_dongle->available_at_ms > ready_at)
				ready_at = coder->right_dongle->available_at_ms;
			wait_ms = (long)(ready_at - elapsed);
			if (wait_ms < 1)
				wait_ms = 1;
			if (get_realtime_deadline_ms(&deadline, wait_ms) != 0)
			{
				fprintf(stderr, "coder %d: failed to get wait deadline\n",
					coder->id);
				stop_locked(cdx);
				break ;
			}
			result = pthread_cond_timedwait(&cdx->coordinator_changed,
					&cdx->coordinator_mutex, &deadline);
		}
		else
			result = pthread_cond_wait(&cdx->coordinator_changed,
					&cdx->coordinator_mutex);
		if (result != 0 && result != ETIMEDOUT)
		{
			fprintf(stderr, "coder %d: failed while waiting for dongles\n",
				coder->id);
			stop_locked(cdx);
			break ;
		}
	}
	pthread_mutex_unlock(&cdx->coordinator_mutex);
	return (0);
}

static int	wait_for_duration(struct codexion_struct *cdx, long duration_ms)
{
	struct timespec	deadline;
	int64_t			start;
	int64_t			elapsed;
	int64_t			remaining;
	int				result;

	result = pthread_mutex_lock(&cdx->coordinator_mutex);
	if (result != 0)
	{
		fprintf(stderr, "coder: failed to lock coordinator\n");
		return (0);
	}
	start = get_time_elapsed_ms(cdx);
	if (start < 0)
	{
		fprintf(stderr, "coder: failed to read elapsed time\n");
		stop_locked(cdx);
		pthread_mutex_unlock(&cdx->coordinator_mutex);
		return (0);
	}
	while (!cdx->stop_requested)
	{
		elapsed = get_time_elapsed_ms(cdx);
		if (elapsed < 0)
		{
			fprintf(stderr, "coder: failed to read elapsed time\n");
			stop_locked(cdx);
			break ;
		}
		remaining = duration_ms - (elapsed - start);
		if (remaining <= 0)
		{
			pthread_mutex_unlock(&cdx->coordinator_mutex);
			return (1);
		}
		if (get_realtime_deadline_ms(&deadline, (long)remaining) != 0)
		{
			fprintf(stderr, "coder: failed to get action deadline\n");
			stop_locked(cdx);
			break ;
		}
		result = pthread_cond_timedwait(&cdx->coordinator_changed,
				&cdx->coordinator_mutex, &deadline);
		if (result != 0 && result != ETIMEDOUT)
		{
			fprintf(stderr, "coder: failed while waiting for action\n");
			stop_locked(cdx);
			break ;
		}
	}
	pthread_mutex_unlock(&cdx->coordinator_mutex);
	return (0);
}

static int	all_coders_done(struct codexion_struct *cdx)
{
	int	i;

	i = 0;
	while (i < cdx->config.nb_coders)
	{
		if (cdx->coders[i].compile_count
			< cdx->config.nb_compiles_required)
			return (0);
		i++;
	}
	return (1);
}

static int	set_coder_state(t_coder *coder, t_coder_state state)
{
	struct codexion_struct	*cdx;
	int						result;

	cdx = coder->cdx;
	result = pthread_mutex_lock(&cdx->coordinator_mutex);
	if (result != 0)
	{
		fprintf(stderr, "coder %d: failed to lock coordinator\n", coder->id);
		return (0);
	}
	if (cdx->stop_requested)
	{
		pthread_mutex_unlock(&cdx->coordinator_mutex);
		return (0);
	}
	coder->state = state;
	if (state == REFACTORING)
		log_event_locked(cdx, coder->id, "is refactoring");
	pthread_cond_broadcast(&cdx->coordinator_changed);
	pthread_mutex_unlock(&cdx->coordinator_mutex);
	return (1);
}

void	*coder_thr_fn(void *arg)
{
	t_coder					*coder;
	struct codexion_struct	*cdx;
	int64_t					elapsed;
	int						compile_finished;
	int						result;

	coder = (t_coder *)arg;
	cdx = coder->cdx;
	while (acquire_dongles(coder))
	{
		compile_finished = wait_for_duration(cdx, cdx->config.tm_compile);
		result = pthread_mutex_lock(&cdx->coordinator_mutex);
		if (result != 0)
		{
			fprintf(stderr, "coder %d: failed to lock coordinator\n",
				coder->id);
			return (NULL);
		}
		elapsed = get_time_elapsed_ms(cdx);
		coder->left_dongle->in_use = false;
		coder->right_dongle->in_use = false;
		if (elapsed >= 0)
		{
			coder->left_dongle->available_at_ms
				= elapsed + cdx->config.dongle_cooldown;
			coder->right_dongle->available_at_ms
				= elapsed + cdx->config.dongle_cooldown;
		}
		else
			stop_locked(cdx);
		if (compile_finished < 0)
			stop_locked(cdx);
		if (compile_finished > 0 && !cdx->stop_requested)
		{
			coder->compile_count++;
			if (coder->compile_count >= cdx->config.nb_compiles_required)
				coder->state = DONE;
			else
			{
				coder->state = DEBUGGING;
				log_event_locked(cdx, coder->id, "is debugging");
			}
			if (all_coders_done(cdx))
				stop_locked(cdx);
		}
		pthread_cond_broadcast(&cdx->coordinator_changed);
		result = !cdx->stop_requested && compile_finished > 0
			&& coder->state == DEBUGGING;
		pthread_mutex_unlock(&cdx->coordinator_mutex);
		if (!result)
			break ;
		if (!wait_for_duration(cdx, cdx->config.tm_debug)
			|| !set_coder_state(coder, REFACTORING)
			|| !wait_for_duration(cdx, cdx->config.tm_refactor)
			|| !set_coder_state(coder, IDLE))
			break ;
	}
	return (NULL);
}
