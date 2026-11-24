# include "codexion.h"

static void	runtime(struct codexion_struct *cdx);
static void	request_stop(struct codexion_struct *cdx);

int	codexion(long int argc, char **argv)
{
	struct codexion_struct	*cdx;
	t_config				config;
	int						parse_code;
	int						result;

	if (argc != 9)
		return (print_to_stderr("[ERROR] expected 8 arguments."));
	parse_code = parse_arguments(argv, &config);
	if (parse_code < 0)
		return (parse_code);
	cdx = init_codexion_struct(&config);
	if (cdx == NULL)
		return (-30);
	result = allocate_arrays(cdx);
	if (result < 0)
	{
		free_codexion_struct(cdx);
		return (result);
	}
	result = pthread_create(&cdx->monitor_thread, NULL, mont_thr_fn, cdx);
	if (result != 0)
	{
		print_to_stderr("failed to create monitor thread");
		request_stop(cdx);
		while (cdx->coder_threads_started > 0)
			pthread_join(cdx->coders[--cdx->coder_threads_started].thread, NULL);
		free_codexion_struct(cdx);
		return (-32);
	}
	runtime(cdx);
	while (cdx->coder_threads_started > 0)
		pthread_join(cdx->coders[--cdx->coder_threads_started].thread, NULL);
	pthread_join(cdx->monitor_thread, NULL);
	free_codexion_struct(cdx);
	return (1);
}

static void	runtime(struct codexion_struct *cdx)
{
	int	result;

	result = pthread_mutex_lock(&cdx->coordinator_mutex);
	if (result != 0)
	{
		fprintf(stderr, "runtime: failed to lock coordinator\n");
		return ;
	}
	while (!cdx->stop_requested)
	{
		result = pthread_cond_wait(&cdx->coordinator_changed,
				&cdx->coordinator_mutex);
		if (result != 0)
		{
			fprintf(stderr, "runtime: failed to wait on coordinator\n");
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			break ;
		}
	}
	pthread_mutex_unlock(&cdx->coordinator_mutex);
}

static void	request_stop(struct codexion_struct *cdx)
{
	pthread_mutex_lock(&cdx->coordinator_mutex);
	cdx->stop_requested = true;
	pthread_cond_broadcast(&cdx->coordinator_changed);
	pthread_mutex_unlock(&cdx->coordinator_mutex);
}
