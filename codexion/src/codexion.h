#ifndef CODEXION_H
# define CODEXION_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <stdint.h>
# include <string.h>
# include <pthread.h>
# include <time.h>
# include <sys/time.h>
# include <stdbool.h>


// Dongle Struct
typedef struct dongle_struct
{
	long int		*id;
	pthread_t		thread;
	pthread_mutex_t	mutex;

}	t_dongle;

// Coder Struct
typedef struct coder_struct
{
	int			id;
	pthread_t	thread;
	t_dongle	*left_dongle;
	t_dongle	*right_dongle;
	char		state;

}	t_coder;

typedef struct s_list
{
	void *content;
	struct s_list *next;
	struct s_list *previous;
} t_list;

// Project struct
struct	codexion_struct {
	// System variables
	int			argc;
	char 		**arguments;
	// Inputted variables
	int 		nb_coders;
	int 		nb_compiles;
	long int 	tm_burnout;
	long int 	tm_compile;
	long int 	tm_debug;
	long int 	tm_refactor;
	long int 	dongle_cooldown;
	char 		*scheduler;
	struct 		timeval	start_time;
	struct 		timeval	current_time;
	// Threads
	pthread_t	monitor_thread;
	// Arrays
	t_dongle	*dongles;
	t_coder		*coders;
};

// Parcer Utils
int		ft_isdigit(int c);
int		ft_atoi(const char *str);
int		ft_strcmp(const char *s1, const char *s2);
int		ft_strlen(const char *str);
char	*ft_strdup(const char *src);

// Debug Utils
void	print_struct(struct codexion_struct *cdx);

// Time Utils
long int	get_time_elapsed_ms(struct codexion_struct *cdx);

// Declare Utils
struct	codexion_struct *init_codexion_struct(int argc, char *argv[]);
void	free_codexion_struct(struct codexion_struct *cdx);
void	allocate_arrays(struct codexion_struct *cdx);

// Parcer
int		parse_arguments(struct codexion_struct *cdx);
void	fill_struct(struct codexion_struct *cdx);
int		validate_numbers(struct codexion_struct *cdx);

// Codexion main function
int		codexion(long int argc, char** arguments);
void	runtime(struct codexion_struct *cdx);

// Monitoring Threads
void	*mont_thr_fn(void *arg);

// Coder Threads
void	*coder_thr_fn(void *arg);

//Lists functions
void	lstadd_back(t_list **lst, t_list *new);
void	lstadd_front(t_list **lst, t_list *new);
void	lstclear(t_list **lst, void (*del)(void*));
void	lstdelone(t_list **lst, t_list *node, void (*del)(void *));

void	lstiter(t_list *lst, void (*f)(void *));
t_list	*lstlast(t_list *lst);
t_list	*lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));
t_list	*lstnew(void *content);
int	lstsize(t_list *lst);



#endif
