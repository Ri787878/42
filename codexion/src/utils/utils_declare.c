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
	i = 0;
	while (cdx->nb_coders[i] != NULL){
		free(cdx->dongles);
		free(cdx->coders);
		i++;
	}
    free(cdx->arguments);
    free(cdx);
}

int	allocate_arrays(struct codexion_struct *cdx){
	cdx->dongles = malloc(cdx->nb_coders * sizeof(*cdx->dongles));
	if (cdx->dongles == NULL)
		return (-31);
	cdx->coders = malloc(cdx->nb_coders * sizeof(*cdx->coders));
	if (cdx->coders == NULL){
		free(cdx->dongles);
		cdx->dongles = NULL;
		return (-32);
	}
}
