# include "../codexion.h"

static int	is_valid_number(const char *str)
{
	int	i;

	if (str == NULL || str[0] == '\0')
		return (0);
	i = 0;
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (str[i] == '\0')
		return (0);
	while (str[i] != '\0')
	{
		if (!ft_isdigit(str[i]))
			return (0);
		i++;
	}
	return (1);
}

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
		// Check if not a number
		if (!is_valid_number(cdx->arguments[c])){
			printf("[PARCING ERROR CODE -2] Argument \"%s\" type is not an int!\n", cdx->arguments[c]);
			return (-2);
		}
		// Check if valid number

		c++;
	}
	if (cdx->arguments[c] == NULL
		|| (strcmp(cdx->arguments[c], "fifo")
			&& strcmp(cdx->arguments[c], "edf"))){
		printf("[PARCING ERROR CODE -3] Scheduler argument \"%s\" isn't \"fifo\" or \"edf\"!\n", cdx->arguments[c]);
		return (-3);
	}
	fill_struct(cdx);
	return (1);
}
