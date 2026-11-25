/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parcer.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:58:36 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 12:17:51 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"
#include <errno.h>
#include <limits.h>

static int	parse_number(const char *arg, long *number);
static int	set_config(t_config *config, long *numbers, t_scheduler scheduler);

int	parse_arguments(char **argv, t_config *config)
{
	long		numbers[7];
	t_scheduler	scheduler;
	int			i;

	if (argv == NULL || config == NULL || argv[8] == NULL)
		return (-20);
	i = 0;
	while (i < 7)
	{
		if (parse_number(argv[i + 1], &numbers[i]) < 0)
			return (print_to_stderr(
					"[ERROR] Numeric arguments must be non negative ints."));
		if (numbers[i] < 0 || (i == 0
				&& (numbers[i] == 0 || numbers[i] > INT_MAX)))
			return (print_to_stderr(
					"[ERROR] Numeric argument is out of range."));
		i++;
	}
	if (strcmp(argv[8], "fifo") == 0)
		scheduler = FIFO;
	else if (strcmp(argv[8], "edf") == 0)
		scheduler = EDF;
	else
		return (print_to_stderr("[ERROR] Scheduler must be fifo or edf."));
	return (set_config(config, numbers, scheduler));
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

static int	set_config(t_config *config, long *numbers, t_scheduler scheduler)
{
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
