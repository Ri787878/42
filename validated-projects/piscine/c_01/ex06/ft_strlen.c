/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 16:46:40 by ridias            #+#    #+#             */
/*   Updated: 2025/09/16 10:50:22 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
		n++;
	return (n);
}

/*
#include <stdio.h>

int main(void)
{
	char	str[] = "Maria is really nice!!";
	int	n;

	n = ft_strlen(str);
	printf("The sentense -> %s <- has %d letters.", str, n);
	return (0);
}
*/