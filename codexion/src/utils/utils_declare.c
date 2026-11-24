# include "../codexion.h"


struct codexion_struct	*init_codexion_struct(t_config	*configs)
{
    struct codexion_struct *cdx;

	if (configs == NULL)
		return (NULL);
	cdx = calloc(1, sizeof(struct codexion_struct));
	if (!cdx)
		return (NULL);
	cdx->config = *configs;
	cdx->coder_mutexes_initialized = 0;
	atomic_init(&cdx->stop_requested, false);
	if (clock_gettime(CLOCK_MONOTONIC, &cdx->start_time) != 0
		|| clock_gettime(CLOCK_MONOTONIC, &cdx->current_time) != 0)
	{
		free(cdx);
		return (NULL);
	}

    return cdx;
}

void free_codexion_struct(struct codexion_struct *cdx)
{
    int i;

    if (cdx == NULL)
        return;

    i = 0;
    while (i < cdx->argc && cdx->arguments != NULL){
		free(cdx->arguments[i]);
		i++;
	}
    free(cdx->arguments);
	if (cdx->coders != NULL)
	{
		i = 0;
		while (i < cdx->coder_mutexes_initialized)
			pthread_mutex_destroy(&cdx->coders[i++].mutex);
	}
    free(cdx->dongles);
    free(cdx->coders);
    free(cdx);
}

int	allocate_arrays(struct codexion_struct *cdx){
	int i;

	i = 0;
	cdx->dongles = malloc(cdx->config.nb_coders * sizeof(*cdx->dongles));
	if (cdx->dongles == NULL)
		return (-31);
	cdx->coders = malloc(cdx->config.nb_coders * sizeof(*cdx->coders));
	if (cdx->coders == NULL){
		free(cdx->dongles);
		cdx->dongles = NULL;
		return (-32);
	}
	while (i < cdx->config.nb_coders){
		cdx->dongles[i].id = i + 1;

		cdx->coders[i].id = i + 1;
		cdx->coders[i].left_dongle = &cdx->dongles[i];
		cdx->coders[i].right_dongle = &cdx->dongles[(i + 1) % cdx->config.nb_coders];
		cdx->coders[i].state = 1;
		cdx->coders[i].cooldown = 0;
		cdx->coders[i].tm_lst_compile = 0;
		i++;
	}
	i = 0;
	while (i < cdx->config.nb_coders)
	{
		if (pthread_mutex_init(&cdx->coders[i].mutex, NULL) != 0)
			return (-33);
		cdx->coder_mutexes_initialized++;
		i++;
	}
	i = 0;
	while (i < cdx->config.nb_coders)
	{
		if (pthread_create(&cdx->coders[i].thread, NULL, coder_thr_fn, NULL) != 0)
		{
			while (i > 0)
				pthread_join(cdx->coders[--i].thread, NULL);
			return (-34);
		}
		i++;
	}
	return (1);
}

int	print_to_stderr(const char *msg)
{
	fprintf(stderr, "Error: %s\n", msg);
	return (-1);
}
