# include "../codexion.h"


void	*coder_thr_fn(void *arg){
	(void) arg;
	printf("Hello from coders!\n");
	pthread_exit(NULL);
	return (NULL);

}
