# include "../codexion.h"

void	*mont_thr_fn(void *arg){
	(void) arg;
	printf("Hello from monitoring!\n");
	pthread_exit(NULL);
	return (NULL);
}
