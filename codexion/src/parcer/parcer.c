# include "../codexion.h"


void fill_struct(struct codexionStruct *cdx){
	cdx->nb_coders = ft_atoi(cdx->arguments[1]);
	cdx->tm_burnout = ft_atoi(cdx->arguments[2]);
	cdx->tm_compile = ft_atoi(cdx->arguments[3]);
	cdx->tm_debug = ft_atoi(cdx->arguments[4]);
	cdx->tm_refactor = ft_atoi(cdx->arguments[5]);
	cdx->nb_compiles = ft_atoi(cdx->arguments[6]);
	cdx->dongle_cooldown = ft_atoi(cdx->arguments[7]);
	cdx->scheduler = cdx->arguments[8];
}


int parse_arguments(struct codexionStruct *cdx)
{
	int c;

	c = 1;
	if (cdx == NULL || cdx->arguments == NULL)
		return (-2);
	if (cdx->argc != 9)
		return (-9);
	while (c <= 7){
		if (cdx->arguments[c] == NULL)
			return (-2);
		// Check if not a number
		if (ft_isdigit(ft_atoi(cdx->arguments[c]))){
			printf("round %d: [PARCING ERROR CODE -2] Argument type is not an int!", c);
			return (-2);
		}
		// Check if valid number

		c++;
	}
	if (cdx->arguments[c] == NULL
		|| (ft_strcmp(cdx->arguments[c], "fifo")
			&& ft_strcmp(cdx->arguments[c], "edf"))){
		printf("[PARCING ERROR CODE -3] Scheduler argument is \"fifo\" or \"edf\"!");
		return (-3);
	}
	fill_struct(cdx);
	return (1);
}
