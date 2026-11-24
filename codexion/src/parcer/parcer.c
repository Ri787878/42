# include "../codexion.h"

# include <errno.h>
# include <limits.h>

static int	parse_number(const char *arg, long *number);


int	parse_arguments(char **argv, t_config *config)
{
	long		numbers[7];
	t_scheduler	scheduler;
	int			result;
	int			i;

	if (argv == NULL)
		return (-22);
	if (config == NULL)
		return (-30);
	i = 0;
	while (i < 7)
	{
		result = parse_number(argv[i + 1], &numbers[i]);
		if (result == -22)
		{
			print_to_stderr("[ERROR] Numeric arguments must be integers.");
			return (-22);
		}
		if (result == -24)
		{
			print_to_stderr("[ERROR] Numeric argument is out of range.");
			return (-24);
		}
		if (numbers[i] < 0 || (i == 0
				&& (numbers[i] == 0 || numbers[i] > INT_MAX)))
		{
			print_to_stderr("[ERROR] Numeric argument is out of range.");
			return (-24);
		}
		i++;
	}
	if (argv[8] == NULL)
		return (-22);
	if (strcmp(argv[8], "fifo") == 0)
		scheduler = FIFO;
	else if (strcmp(argv[8], "edf") == 0)
		scheduler = EDF;
	else
	{
		print_to_stderr("[ERROR] Scheduler must be fifo or edf.");
		return (-23);
	}
	config->nb_coders = (int)numbers[0];
	config->tm_burnout = numbers[1];
	config->tm_compile = numbers[2];
	config->tm_debug = numbers[3];
	config->tm_refactor = numbers[4];
	config->nb_compiles_required = numbers[5];
	config->dongle_cooldown = numbers[6];
	config->scheduler = scheduler;
	return (1);
}

static int	parse_number(const char *arg, long *number)
{
	const char	*cursor;

	if (arg == NULL || arg[0] == '\0')
		return (-22);
	cursor = arg;
	if (*cursor == '+' || *cursor == '-')
		cursor++;
	if (*cursor < '0' || *cursor > '9')
		return (-22);
	while (*cursor >= '0' && *cursor <= '9')
		cursor++;
	if (*cursor != '\0')
		return (-22);
	errno = 0;
	*number = strtol(arg, NULL, 10);
	if (errno == ERANGE)
		return (-24);
	return (1);
}
