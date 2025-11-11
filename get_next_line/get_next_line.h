/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:48 by ridias            #+#    #+#             */
/*   Updated: 2025/11/11 15:18:39 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stdlib.h>
# include <unistd.h>

# define BUFFER_SIZE 42
char	*get_next_line(int fd);

void	ft_putstr(char *str);
size_t	ft_strlen(const char *str);
size_t	ft_strlcpy(char *dst, const char *src, size_t size);
size_t	find_new_line(const char *s);
char	*ft_strdup(const char *src);
char	*ft_strjoin(const char *s1, const char *s2);
char	*ft_substr(char const *s, unsigned int start, size_t len);

#endif
