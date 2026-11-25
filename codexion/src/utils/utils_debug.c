/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_debug.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:57:56 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 09:57:57 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../codexion.h"

//void	print_struct(struct codexion_struct *cdx)
//{
//	int	i;

//	i = 0;
//	printf("\n[%" PRIi64 "] cdx.nb_coders = %d\n",
//		get_time_elapsed_ms(cdx), cdx->config.nb_coders);
//	printf("cdx->config.tm_burnout = %ld\n",
//		cdx->config.tm_burnout);
//	printf("cdx->config.tm_compile = %ld\n",
//		cdx->config.tm_compile);
//	printf("cdx->config.tm_debug = %ld\n",
//		cdx->config.tm_debug);
//	printf("cdx->config.tm_refactor = %ld\n",
//		cdx->config.tm_refactor);
//	printf("cdx->config.nb_compiles_required = %ld\n",
//		cdx->config.nb_compiles_required);
//	printf("cdx->config.scheduler = %d\n",
//		(int)cdx->config.scheduler);
//	printf("cdx->config.dongles = %zu\n", sizeof(cdx->dongles));
//	while (i < cdx->config.nb_coders)
//	{
//		printf("\ncoder id = %ld\n", cdx->dongles[i].id);
//		printf("coder %ld left_dongle.id = %ld\n",
//			cdx->dongles[i].id, cdx->coders[i].left_dongle->id);
//		printf("coder %ld right_dongle.id = %ld\n",
//			cdx->dongles[i].id, cdx->coders[i].right_dongle->id);
//		printf("coder %ld state = %d\n",
//			cdx->dongles[i].id, cdx->coders[i].state);
//		printf("coder %ld cooldown = %ld\n",
//			cdx->dongles[i].id, cdx->coders[i].cooldown);
//		printf("coder %ld cooldown = %ld\n",
//			cdx->dongles[i].id, cdx->coders[i].tm_lst_compile);
//		i++;
//	}
//	printf("\n\nElapsed time %" PRIi64 "\n", get_time_elapsed_ms(cdx));
//}if

void	log_event_locked(struct codexion_struct *cdx, int coder_id,
		const char *message){
	int64_t	elapsed;

	elapsed = get_time_elapsed_ms(cdx);
	if (elapsed < 0)
	{
		fprintf(stderr, "log: failed to read elapsed time\n");
		return ;
	}
	printf("%" PRIi64 " %d %s\n", elapsed, coder_id, message);
}
