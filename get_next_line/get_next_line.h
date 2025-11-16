/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:48 by ridias            #+#    #+#             */
/*   Updated: 2025/11/16 14:28:51 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stdlib.h>
# include <unistd.h>

# define BUFFER_SIZE 42

char	*get_next_line(int fd);
int		find_new_line(const char *s);
size_t	ft_strlen(const char *str);
char	*ft_strdup(const char *src);
void	*ft_calloc(size_t number, size_t size);
char	*ft_strjoin(const char *s1, const char *s2);
void	ft_bzero(void *s, size_t n);


#endif
