/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:35:19 by ridias            #+#    #+#             */
/*   Updated: 2025/11/14 00:17:54 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		counter;
	int		t;

	t = 0;
	counter = 0;
	va_start(args, format);
	while (format[t] != '\0')
	{
		if (format[t] == '%')
		{
			t++;
			if (format[t] == '\0')
				break ;
			counter += check_char(format, t, args);
			t++;
		}
		else
			counter += ft_putchar(format[t++]);
	}
	va_end(args);
	return (counter);
}
