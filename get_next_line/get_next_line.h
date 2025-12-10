/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 11:06:48 by ridias            #+#    #+#             */
/*   Updated: 2025/12/10 15:02:34 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>

# define BUFFER_SIZE 42

char	*get_next_line(int fd);
int		clean_check_new_line(char *buffer);
size_t	ft_strlen(const char *str);

#endif
