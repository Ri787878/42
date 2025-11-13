/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:35:19 by ridias            #+#    #+#             */
/*   Updated: 2025/11/13 16:36:45 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	check_char(const char *format, int t, va_list args)
{
	if (format[t] == 'c')
		return (ft_putchar(va_arg(args, int)));
	if (format[t] == 's')
		return (ft_putstr(va_arg(args, char *)));
	if (format[t] == 'p')
	{
		//create func for pointer version
	}
	if (format[t] == 'd')
	{
		return (ft_putnbr(va_arg(args, int)));
	}
	if (format[t] == 'u')
	{
		//create func for version
	}
	if (format[t] == 'x')
	{
		//create func for version
	}
	if (format[t] == 'X')
	{
		//create func for version
	}
	if (format[t] == '%')
		return (ft_putchar(format[t]));
	else
		return (0);
}

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
			counter += check_char(format, t, args);
			t++;
		}
		else
			counter += ft_putchar(format[t++]);
	}
	va_end(args);
	return (counter);
}
