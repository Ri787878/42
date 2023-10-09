/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/08/10 12:15:14 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/08/10 12:15:19 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}
/*
int main (void)
{
	int	n1;
	int	n2;
	char	*w1 = "Ma11';' /ria";

	n1 = ft_strlen(w1);
	n2 = strlen(w1);
	printf("a minha versao %d, a correta %d.", n1, n2);
}
*/
