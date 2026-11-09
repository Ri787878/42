# include "../codexion.h"


void	print_struct(struct codexionStruct *cdx){
	printf("cdx.nb_coders = %d\n", cdx->nb_coders);
	printf("cdx.tm_burnout = %ld\n", cdx->tm_burnout);
	printf("cdx.tm_compile = %ld\n", cdx->tm_compile);
	printf("cdx.tm_debug = %ld\n", cdx->tm_debug);
	printf("cdx.tm_refactor = %ld\n", cdx->tm_refactor);
	printf("cdx.nb_compiles = %d\n", cdx->nb_compiles);
	printf("cdx.dongle_cooldown = %ld\n", cdx->dongle_cooldown);
	printf("cdx.scheduler = %s\n", cdx->scheduler);
}
