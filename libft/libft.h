/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/09 14:57:00 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:22:27 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef ALL
#define All
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stddef.h>

int	ft_atoi(char *str);
void	ft_bzero(void *s, size_t n);
void* ft_calloc( size_t num, size_t size );
int	ft_isalnum(int c);
int	ft_isalpha(int c);
int	ft_isascii(int c);
int	ft_isdigit(int c);
int	ft_isprint(int c);
void	*ft_memchr( const void *ptr, int ch, size_t count);
int	ft_memcmp( const void* w1, const void* w2, size_t count );
void	*ft_memcpy(void *dest, const void *src, size_t n);
void	*ft_memmove(void *dest, const void *src, size_t n);
void	*ft_memset(void *s, int c, size_t n);
char	*ft_strchr	(const char *s, int c);
char * ft_strdup( const char *str1 );
size_t	ft_strlcat	(char	*dst, const	char *src, size_t	size);
size_t	ft_strlcpy	(char *dst, const char *src, size_t size);
int	ft_strlen(char *str);
int	ft_strncmp(char *s1, char *s2, unsigned int n);
char	*ft_strnstr(const char *haystack, const char *needle, size_t len);
char	*ft_strrchr	(const char *s, int c);
char *ft_substr(char const *s, unsigned int start, size_t len);
char	ft_tolower	(char c);
char	ft_toupper	(char c);













#endif
