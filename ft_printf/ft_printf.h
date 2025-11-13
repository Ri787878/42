/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 16:46:39 by ridias            #+#    #+#             */
/*   Updated: 2025/11/13 16:41:26 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdlib.h>
# include <unistd.h>
# include <stdarg.h>

int		ft_putnbr(int nb);
int		ft_putstr(char *s);
int		ft_putchar(const char c);
int		ft_printf(const char *format, ...);
int		check_char(const char *format, int t, va_list args);

#endif
