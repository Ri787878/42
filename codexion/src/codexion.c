# include "codexion.h"


static void	runtime(struct codexion_struct *cdx);

int	codexion(long int argc, char** argv)
{
	struct		codexion_struct *cdx;
	t_config	config;
	int			i;
	int			parse_code;

	if (argc != 9)
		return (print_to_stderr("[ERROR] expected 8 arguments."));
	parse_code = parse_arguments(argv, &config);
	if (parse_code < 0)
		return (parse_code);
	cdx = init_codexion_struct(&config);
	if (cdx == NULL)
		return (-30);
	if (allocate_arrays(cdx) < 0) {
		free_codexion_struct(cdx);
		return (-31);
	}
	if (pthread_create(&cdx->monitor_thread, NULL, mont_thr_fn, cdx) != 0)
	{
		print_to_stderr("failed to create monitor thread\n");
		atomic_store(&cdx->stop_requested, true);
		i = 0;
		while (i < cdx->config.nb_coders)
			pthread_join(cdx->coders[i++].thread, NULL);
		free_codexion_struct(cdx);
		return (-32);
	}
	runtime(cdx);
	i = 0;
	while (i < cdx->config.nb_coders)
		pthread_join(cdx->coders[i++].thread, NULL);
	pthread_join(cdx->monitor_thread, NULL);
	print_struct(cdx);
	free_codexion_struct(cdx);
	return (1);
}

static void	runtime(struct codexion_struct *cdx){
	int	i;

	i = 0;
	while (i < cdx->config.nb_compiles_required
		&& !atomic_load(&cdx->stop_requested)){
		print_struct(cdx);
		sleep(2);
		printf("\n\nprint after 2 seconds\n\n");
		i++;
	}
	atomic_store(&cdx->stop_requested, true);
}
