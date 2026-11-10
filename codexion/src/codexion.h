#ifndef CODEXION_H
# define CODEXION_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <stdint.h>
#include <string.h>


// Project struct
struct	codexionStruct {
	// System variables
	int argc;
	char **arguments;
	// Inputted variables
	int nb_coders;
	int nb_compiles;
	long int tm_burnout;
	long int tm_compile;
	long int tm_debug;
	long int tm_refactor;
	long int dongle_cooldown;
	char *scheduler;
};

// Parcer Utils
int		ft_isdigit(int c);
int		ft_atoi(const char *str);
int		ft_strcmp(const char *s1, const char *s2);
int		ft_strlen(const char *str);
char	*ft_strdup(const char *src);

// Debug Utils
void	print_struct(struct codexionStruct *cdx);

// Declare Utils
struct	codexionStruct *init_codexion_struct(int argc, char *argv[]);
void	free_codexion_struct(struct codexionStruct *cdx);

// Parcer
int		parse_arguments(struct codexionStruct *cdx);
void	fill_struct(struct codexionStruct *cdx);
int		validate_numbers(struct codexionStruct *cdx);

// Codexion main function
int		codexion(long int argc, char** arguments);

#endif
