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

int64_t	convert_to_ms(struct timespec time){
	return ((int64_t)time.tv_sec * 1000
		+ time.tv_nsec / 1000000);
}
