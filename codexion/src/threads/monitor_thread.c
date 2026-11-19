# include "../codexion.h"

void	*mont_thr_fn(void *cdx){
	int	i;

	i = 0;
	while (i < 4){
		sleep(1);
		printf("%" PRIi64 " Monitoring Thread is running...\n",
			get_time_elapsed_ms((struct codexion_struct *)cdx));
		i++;
	}
	pthread_exit(NULL);
	return (NULL);
}
