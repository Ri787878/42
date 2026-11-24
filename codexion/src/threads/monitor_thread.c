# include "../codexion.h"

# include <errno.h>

void	*mont_thr_fn(void *arg)
{
	struct codexion_struct	*cdx;
	struct timespec			deadline;
	int64_t					elapsed;
	int						i;
	int						burned_out;
	int						result;

	cdx = (struct codexion_struct *)arg;
	result = pthread_mutex_lock(&cdx->coordinator_mutex);
	if (result != 0)
	{
		fprintf(stderr, "monitor: failed to lock coordinator\n");
		return (NULL);
	}
	while (!cdx->stop_requested)
	{
		elapsed = get_time_elapsed_ms(cdx);
		if (elapsed < 0)
		{
			fprintf(stderr, "monitor: failed to read elapsed time\n");
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			break ;
		}
		i = 0;
		burned_out = 0;
		while (i < cdx->config.nb_coders)
		{
			if (cdx->coders[i].state != DONE
				&& elapsed - cdx->coders[i].tm_lst_compile
				>= cdx->config.tm_burnout)
			{
				burned_out = 1;
				break ;
			}
			i++;
		}
		if (burned_out)
		{
			log_event_locked(cdx, cdx->coders[i].id, "burned out");
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			break ;
		}
		if (get_realtime_deadline_ms(&deadline, 1) != 0)
		{
			fprintf(stderr, "monitor: failed to get wait deadline\n");
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			break ;
		}
		result = pthread_cond_timedwait(&cdx->coordinator_changed,
				&cdx->coordinator_mutex, &deadline);
		if (result != 0 && result != ETIMEDOUT)
		{
			fprintf(stderr, "monitor: failed to wait on coordinator\n");
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			break ;
		}
	}
	pthread_mutex_unlock(&cdx->coordinator_mutex);
	return (NULL);
}
