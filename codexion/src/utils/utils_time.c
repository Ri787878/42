/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_time.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:59:16 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 10:01:06 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"

int64_t	get_time_elapsed_ms(struct codexion_struct *cdx)
{
	struct timespec	current_time;

	if (cdx == NULL)
		return (-1);
	if (clock_gettime(CLOCK_MONOTONIC, &current_time) != 0)
		return (-1);
	return ((int64_t)(current_time.tv_sec - cdx->start_time.tv_sec) * 1000
		+ (int64_t)(current_time.tv_nsec - cdx->start_time.tv_nsec) / 1000000);
}

int64_t	convert_to_ms(struct timespec time)
{
	return ((int64_t)time.tv_sec * 1000
		+ time.tv_nsec / 1000000);
}

int	get_realtime_deadline_ms(struct timespec *deadline, long wait_ms)
{
	struct timeval	now;

	if (deadline == NULL || wait_ms < 0 || gettimeofday(&now, NULL) != 0)
		return (-1);
	deadline->tv_sec = now.tv_sec + wait_ms / 1000;
	deadline->tv_nsec = now.tv_usec * 1000
		+ (wait_ms % 1000) * 1000000;
	if (deadline->tv_nsec >= 1000000000)
	{
		deadline->tv_sec++;
		deadline->tv_nsec -= 1000000000;
	}
	return (0);
}
