# include "../codexion.h"


struct codexion_struct	*init_codexion_struct(int argc, char *argv[])
{
    struct codexion_struct *cdx;
	int i;

	if (argc < 1)
		return (NULL);
	cdx = malloc(sizeof(struct codexion_struct));
	if (!cdx)
		return (NULL);
	cdx->argc = argc;
	cdx->arguments = NULL;
	cdx->dongles = NULL;
	cdx->coders = NULL;
	cdx->coder_mutexes_initialized = 0;
	atomic_init(&cdx->stop_requested, false);
	if (argc != 9 || argv == NULL)
		return (cdx);
	cdx->arguments = malloc(argc * sizeof(char *));
    if (!cdx->arguments){
		free(cdx);
		return (NULL);
	}

	// fill arguments in struct with argv
	i = 0;
    while (i < argc) {
		if (argv[i] == NULL) {
			cdx->arguments[i] = NULL;
			i++;
			continue;
		}
        cdx->arguments[i] = ft_strdup(argv[i]);
		if (!cdx->arguments[i]) {
			while (i > 0)
				free(cdx->arguments[--i]);
			free(cdx->arguments);
			free(cdx);
			return (NULL);
		}
		i++;
	}
	// create threads

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
	cdx->dongles = malloc(cdx->nb_coders * sizeof(*cdx->dongles));
	if (cdx->dongles == NULL)
		return (-31);
	cdx->coders = malloc(cdx->nb_coders * sizeof(*cdx->coders));
	if (cdx->coders == NULL){
		free(cdx->dongles);
		cdx->dongles = NULL;
		return (-32);
	}
	while (i < cdx->nb_coders){
		cdx->dongles[i].id = i + 1;

		cdx->coders[i].id = i + 1;
		cdx->coders[i].left_dongle = &cdx->dongles[i];
		cdx->coders[i].right_dongle = &cdx->dongles[(i + 1) % cdx->nb_coders];
		cdx->coders[i].state = 1;
		cdx->coders[i].cooldown = 0;
		cdx->coders[i].tm_lst_compile = 0;
		i++;
	}
	i = 0;
	while (i < cdx->nb_coders)
	{
		if (pthread_mutex_init(&cdx->coders[i].mutex, NULL) != 0)
			return (-33);
		cdx->coder_mutexes_initialized++;
		i++;
	}
	i = 0;
	while (i < cdx->nb_coders)
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
