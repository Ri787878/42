# include "../codexion.h"


struct codexionStruct *init_codexion_struct(int argc, char *argv[]) {
    struct codexionStruct *cdx;
	int i;

	if (argc < 1 || argv == NULL)
		return (NULL);
	cdx = malloc(sizeof(struct codexionStruct));
	if (!cdx)
		return (NULL);
	cdx->argc = argc;
	cdx->arguments = malloc(argc * sizeof(char *));
    if (!cdx->arguments){
		free(cdx);
		return (NULL);
	}

	i = 0;
    while (i < argc) {
		if (argv[i] == NULL) {
			while (i > 0)
				free(cdx->arguments[--i]);
			free(cdx->arguments);
			free(cdx);
			return (NULL);
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

    return cdx;
}

void free_codexion_struct(struct codexionStruct *cdx) {
    if (cdx == NULL)
		return;
	int i;

	i = 0;
    while (i < cdx->argc && cdx->arguments != NULL) {
        free(cdx->arguments[i]);
		i++;
    }
    free(cdx->arguments);
	free(cdx);
}
