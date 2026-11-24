# include "codexion.h"


void	runtime(struct codexion_struct *cdx){
	int	i;

	i = 0;
	while (i < cdx->nb_compiles
		&& !atomic_load(&cdx->stop_requested)){
		print_struct(cdx);
		sleep(2);
		printf("\n\nprint after 2 seconds\n\n");
		i++;
	}
	atomic_store(&cdx->stop_requested, true);
}


int	codexion(long int argc, char** argv)
{
	struct		codexion_struct *cdx;
	int			parse_code;
	int			i;

	cdx = init_codexion_struct(argc, argv);
	if (cdx == NULL)
		return (-30);
	parse_code = parse_arguments(cdx);
	if (parse_code <= 0) {
		free_codexion_struct(cdx);
		return (parse_code);
	}
	if (validate_numbers(cdx) < 0) {
		free_codexion_struct(cdx);
		return (-24);
	}
	if (allocate_arrays(cdx) < 0) {
		free_codexion_struct(cdx);
		return (-31);
	}
	if (pthread_create(&cdx->monitor_thread, NULL, mont_thr_fn, cdx) != 0)
	{
		fprintf(stderr, "failed to create monitor thread\n");
		atomic_store(&cdx->stop_requested, true);
		i = 0;
		while (i < cdx->nb_coders)
			pthread_join(cdx->coders[i++].thread, NULL);
		free_codexion_struct(cdx);
		return (-32);
	}

	runtime(cdx);
	i = 0;
	while (i < cdx->nb_coders)
		pthread_join(cdx->coders[i++].thread, NULL);
	pthread_join(cdx->monitor_thread, NULL);
	print_struct(cdx);
	free_codexion_struct(cdx);
	return (1);
}
