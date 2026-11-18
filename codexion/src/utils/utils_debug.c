# include "../codexion.h"


void	print_struct(struct codexion_struct *cdx)
{
	int	i;

	i = 0;
	printf("\n[%ld] cdx.nb_coders = %d\n", get_time_elapsed_ms(cdx), cdx->nb_coders);
	printf("cdx.tm_burnout = %ld\n", cdx->tm_burnout);
	printf("cdx.tm_compile = %ld\n", cdx->tm_compile);
	printf("cdx.tm_debug = %ld\n", cdx->tm_debug);
	printf("cdx.tm_refactor = %ld\n", cdx->tm_refactor);
	printf("cdx.nb_compiles = %d\n", cdx->nb_compiles);
	printf("cdx.dongle_cooldown = %ld\n", cdx->dongle_cooldown);
	printf("cdx.scheduler = %s\n", cdx->scheduler);
	printf("cdx.dongles = %ld\n", sizeof(cdx->dongles));
	while (i < cdx->nb_coders){
		printf("\ncoder id = %ld\n", cdx->dongles[i].id);
		printf("coder %ld left_dongle.id = %ld\n", cdx->dongles[i].id, cdx->coders[i].left_dongle->id);
		printf("coder %ld right_dongle.id = %ld\n", cdx->dongles[i].id, cdx->coders[i].right_dongle->id);
		printf("coder %ld state = %d\n\n", cdx->dongles[i].id, cdx->coders[i].state);
		i++;
	}
	printf("\nElapsed time %ld\n\n", get_time_elapsed_ms(cdx));

}
