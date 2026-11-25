/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/25 09:59:22 by ridias            #+#    #+#             */
/*   Updated: 2026/11/25 09:59:23 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

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
# include <inttypes.h>


// Enum for both types of scheduler
typedef enum e_scheduler
{
	FIFO,
	EDF
}	t_scheduler;

// Enum for coder state
typedef enum e_coder_state
{
	IDLE,
	COMPILING,
	WAITING,
	DEBUGGING,
	REFACTORING,
	DONE
}	t_coder_state;

//Configs Struct
typedef struct s_config
{
	int 		nb_coders;
	long	 	tm_burnout;
	long	 	tm_compile;
	long	 	tm_debug;
	long	 	tm_refactor;
	long	 	nb_compiles_required;
	long	 	dongle_cooldown;
	t_scheduler	scheduler;
}	t_config;

// Dongle Struct
typedef struct dongle_struct
{
	long int		id;
	bool			in_use;
	int64_t			available_at_ms;

}	t_dongle;

// Coder Struct
typedef struct coder_struct
{
	int				id;
	pthread_t		thread;
	struct codexion_struct	*cdx;
	t_dongle		*left_dongle;
	t_dongle		*right_dongle;
	t_coder_state	state;
	long int		cooldown;
	long int		tm_lst_compile;
	long int		compile_count;
	int64_t			request_sequence;

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
	t_config	config;
	struct 		timespec	start_time;
	struct 		timespec	current_time;
	// Threads
	pthread_t	monitor_thread;
	pthread_mutex_t	coordinator_mutex;
	pthread_cond_t	coordinator_changed;
	bool			coordinator_mutex_initialized;
	bool			coordinator_cond_initialized;
	bool			stop_requested;
	int				coder_threads_started;
	int64_t			next_request_sequence;
	// Arrays
	t_dongle	*dongles;
	t_coder		*coders;
};

// Parcer Utils
int		ft_strlen(const char *str);

// Debug Utils
void	print_struct(struct codexion_struct *cdx);
void	log_event_locked(struct codexion_struct *cdx, int coder_id,
			const char *message);

// Time Utils
int64_t	get_time_elapsed_ms(struct codexion_struct *cdx);
int64_t	convert_to_ms(struct timespec time);
int		get_realtime_deadline_ms(struct timespec *deadline, long wait_ms);

// Declare Utils
struct codexion_struct	*init_codexion_struct(t_config	*configs);
void	free_codexion_struct(struct codexion_struct *cdx);
int	allocate_arrays(struct codexion_struct *cdx);
int	print_to_stderr(const char *msg);

// Parcer
int	parse_arguments(char **argv, t_config *configs);


// Codexion main function
int		codexion(long int argc, char** arguments);

// Monitoring Threads
void	*mont_thr_fn(void *arg);

// Coder Threads
void	*coder_thr_fn(void *arg);

//Lists functions
void	lstadd_back(t_list **lst, t_list *new);
void	lstadd_front(t_list **lst, t_list *new);
void	lstclear(t_list **lst, void (*del)(void*));
void	lstdelone(t_list **lst, t_list *node, void (*del)(void *));

int	lstiter(t_list *lst, int (*f)(void *));
t_list	*lstlast(t_list *lst);
t_list	*lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));
t_list	*lstnew(void *content);
int	lstsize(t_list *lst);



#endif
