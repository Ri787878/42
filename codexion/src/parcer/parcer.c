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

void	fill_struct(struct codexion_struct *cdx)
{
	cdx->nb_coders = ft_atoi(cdx->arguments[1]);
	cdx->tm_burnout = ft_atoi(cdx->arguments[2]);
	cdx->tm_compile = ft_atoi(cdx->arguments[3]);
	cdx->tm_debug = ft_atoi(cdx->arguments[4]);
	cdx->tm_refactor = ft_atoi(cdx->arguments[5]);
	cdx->nb_compiles = ft_atoi(cdx->arguments[6]);
	cdx->dongle_cooldown = ft_atoi(cdx->arguments[7]);
	cdx->scheduler = cdx->arguments[8];
	gettimeofday(&cdx->start_time, NULL);
	gettimeofday(&cdx->current_time, NULL);
	pthread_create(&cdx->monitor_thread, NULL, mont_thr_fn, NULL);
	cdx->coders = NULL;
	cdx->dongles = NULL;

}


int	parse_arguments(struct codexion_struct *cdx)
{
	int			c;
	const char	*argument;

	c = 1;
	if (cdx == NULL)
		return (-30);
	if (cdx->argc != 9)
		return (-29);
	if (cdx->arguments == NULL)
		return (-22);
	while (c <= 7){
		// Check if not a number
		if (!is_valid_number(cdx->arguments[c])){
			argument = cdx->arguments[c];
			if (argument == NULL)
			printf("[PARCING ERROR CODE -22] Argument \"(null)\" type is not an int!\n");
			return (-22);
		}
		c++;
	}
	if (cdx->arguments[c] == NULL){
		printf("[PARCING ERROR CODE -22] Scheduler argument is missing!\n");
		return (-22);
	}
	if (strcmp(cdx->arguments[c], "fifo")
		&& strcmp(cdx->arguments[c], "edf")){
		printf("[PARCING ERROR CODE -23] Scheduler argument \"%s\" isn't \"fifo\" or \"edf\"!\n",
			cdx->arguments[c]);
		return (-23);
	}
	fill_struct(cdx);
	return (1);
}

int	validate_numbers(struct codexion_struct *cdx)
{
    if (cdx->nb_coders < 1){
        printf("[PARCING ERROR CODE -40] Number of coders must be more than 0!\n");
        return (-24);
    } else if (cdx->nb_compiles < 0){
        printf("[PARCING ERROR CODE -41] Number of compiles must be more than or equal to 0!\n");
        return (-24);
    } else if (cdx->tm_burnout < 0){
        printf("[PARCING ERROR CODE -42] Number of time_to_burnout must be more than or equal to 0!\n");
        return (-24);
    } else if (cdx->tm_compile < 0){
        printf("[PARCING ERROR CODE -43] Number of time_to_compile must be more than or equal to 0!\n");
        return (-24);
    } else if (cdx->tm_debug < 0){
        printf("[PARCING ERROR CODE -44] Number of time_to_debug must be more than or equal to 0!\n");
        return (-24);
    } else if (cdx->tm_refactor < 0){
        printf("[PARCING ERROR CODE -45] Number of time_to_refactor must be more than or equal to 0!\n");
        return (-24);
    } else if (cdx->dongle_cooldown < 0){
        printf("[PARCING ERROR CODE -46] The dongle_cooldown must be more than or equal to 0!\n");
        return (-24);
    }
    return (1);
}
