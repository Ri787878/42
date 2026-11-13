# include "../codexion.h"

void	*mont_thr_fn(void *arg){
	(void) arg;
	//int	i;

	//i = 0;
	//while (i < 4){
	//	sleep(1);
	//	printf("Thread is running...\n");
	//	i++;
	//}
	printf("\nyey\n");
	pthread_exit(NULL);
	return (NULL);
}
