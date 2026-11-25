/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_declare.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:57:51 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 09:57:52 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"

struct codexion_struct	*init_codexion_struct(t_config	*configs)
{
	struct codexion_struct	*cdx;

	cdx = malloc(sizeof(*cdx));
	if (!cdx || configs == NULL)
		return (NULL);
	memset(cdx, 0, sizeof(*cdx));
	cdx->config = *configs;
	if (pthread_mutex_init(&cdx->coordinator_mutex, NULL) != 0)
		return (free(cdx), NULL);
	cdx->coordinator_mutex_initialized = true;
	if (pthread_cond_init(&cdx->coordinator_changed, NULL) != 0)
	{
		pthread_mutex_destroy(&cdx->coordinator_mutex);
		return (free(cdx), NULL);
	}
	cdx->coordinator_cond_initialized = true;
	if (clock_gettime(CLOCK_MONOTONIC, &cdx->start_time) != 0
		|| clock_gettime(CLOCK_MONOTONIC, &cdx->current_time) != 0)
	{
		pthread_cond_destroy(&cdx->coordinator_changed);
		pthread_mutex_destroy(&cdx->coordinator_mutex);
		free(cdx);
		return (NULL);
	}
	return (cdx);
}

void	free_codexion_struct(struct codexion_struct *cdx)
{
	int	i;

	if (cdx == NULL)
		return ;
	i = 0;
	while (i < cdx->argc && cdx->arguments != NULL)
		free(cdx->arguments[i++]);
	free(cdx->arguments);
	free(cdx->dongles);
	free(cdx->coders);
	if (cdx->coordinator_cond_initialized)
		pthread_cond_destroy(&cdx->coordinator_changed);
	if (cdx->coordinator_mutex_initialized)
		pthread_mutex_destroy(&cdx->coordinator_mutex);
	free(cdx);
}

int	allocate_arrays(struct codexion_struct *cdx)
{
	int	i;

	i = 0;
	cdx->dongles = malloc(cdx->config.nb_coders * sizeof(*cdx->dongles));
	cdx->coders = malloc(cdx->config.nb_coders * sizeof(*cdx->coders));
	if (cdx->dongles == NULL || cdx->coders == NULL)
	{
		free(cdx->dongles);
		free(cdx->coders);
		cdx->dongles = NULL;
		cdx->coders = NULL;
		return (-31);
	}
	memset(cdx->dongles, 0,
		cdx->config.nb_coders * sizeof(*cdx->dongles));
	memset(cdx->coders, 0,
		cdx->config.nb_coders * sizeof(*cdx->coders));
	while (i < cdx->config.nb_coders)
	{
		cdx->dongles[i].id = i + 1;
		cdx->coders[i].id = i + 1;
		cdx->coders[i].cdx = cdx;
		cdx->coders[i].left_dongle = &cdx->dongles[i];
		cdx->coders[i].right_dongle = (
				&cdx->dongles[(i + 1) % cdx->config.nb_coders]);
		cdx->coders[i].state = IDLE;
		cdx->coders[i].cooldown = 0;
		cdx->coders[i].tm_lst_compile = 0;
		i++;
	}
	i = 0;
	while (i < cdx->config.nb_coders)
	{
		if (pthread_create(&cdx->coders[i].thread, NULL, coder_thr_fn,
				&cdx->coders[i]) != 0)
		{
			pthread_mutex_lock(&cdx->coordinator_mutex);
			cdx->stop_requested = true;
			pthread_cond_broadcast(&cdx->coordinator_changed);
			pthread_mutex_unlock(&cdx->coordinator_mutex);
			while (cdx->coder_threads_started > 0)
				pthread_join(cdx->coders[--cdx->coder_threads_started].thread,
					NULL);
			return (-34);
		}
		cdx->coder_threads_started++;
		i++;
	}
	return (1);
}

int	print_to_stderr(const char *msg)
{
	fprintf(stderr, "Error: %s\n", msg);
	return (-1);
}
