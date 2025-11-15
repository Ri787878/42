#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	n;

	n = 0;
	if (size == 0)
		return (ft_strlen(src));
	while (n < size - 1 && src[n] != '\0')
	{
		dst[n] = src[n];
		n++;
	}
	dst[n] = '\0';
	return (ft_strlen(src));
}

char	*extract_line(char **buffer)
{
	int		index;
	char	*overflow;

	index = find_new_line(*buffer);
	overflow = malloc((index + 2) * sizeof(char));
	if (!overflow)
		return (NULL);
	ft_strlcpy(overflow, *buffer, index + 2);
	return (overflow);
}

int main(void)
{
	char	*str = "MARIA ESTAS A JANELA\nCom o teu cabelo";
	char	**str1;
	char	*res;

	str1 = &str;
	res = extract_line(str1);
	printf(" the str \"%s\"\n turns into \"%s\"\n", *str1, res);
	free(res);
	return (0);
}
