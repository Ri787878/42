#include "../codexion.h"


long int	get_time_elapsed_ms(struct codexion_struct *cdx){
	long int time_elapsed;


	if (cdx == NULL)
		return (-1);

	gettimeofday(&cdx->current_time, NULL);
	time_elapsed = (cdx->current_time.tv_sec - cdx->start_time.tv_sec) * 1000
		+ (cdx->current_time.tv_usec - cdx->start_time.tv_usec) / 1000;
	return (time_elapsed);
}
