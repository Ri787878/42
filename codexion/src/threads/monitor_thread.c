# include "../codexion.h"

void	*mont_thr_fn(void *arg)
{
	struct codexion_struct	*cdx;
	struct timespec			poll_interval;
	int64_t					elapsed;
	int						i;
	int						burned_out;

	cdx = (struct codexion_struct *)arg;
	poll_interval.tv_sec = 0;
	poll_interval.tv_nsec = 1000000;
	while (!atomic_load(&cdx->stop_requested))
	{
		elapsed = get_time_elapsed_ms(cdx);
		if (elapsed < 0)
		{
			fprintf(stderr, "monitor: failed to read elapsed time\n");
			atomic_store(&cdx->stop_requested, true);
			break ;
		}
		i = 0;
		burned_out = 0;
		while (i < cdx->config.nb_coders)
		{
			pthread_mutex_lock(&cdx->coders[i].mutex);
			if (elapsed - cdx->coders[i].tm_lst_compile >= cdx->config.tm_burnout)
				burned_out = 1;
			pthread_mutex_unlock(&cdx->coders[i].mutex);
			if (burned_out)
				break ;
			i++;
		}
		if (burned_out)
		{
			atomic_store(&cdx->stop_requested, true);
			break ;
		}
		nanosleep(&poll_interval, NULL);
	}
	return (NULL);
}
