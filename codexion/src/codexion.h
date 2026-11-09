#ifndef CODEXION_H
# define CODEXION_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <stdint.h>

// Parcer Utils
int	ft_isdigit(int c);
int	ft_atoi(const char *str);

// Parcer
int parse_arguments(int argc, char *argv[]);

// Codexion main function
int	codexion(int argc, char** arguments);

#endif
