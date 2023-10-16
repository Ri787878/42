

#include "libft.h"

size_t	ft_strlcat	(char	*dst, const	char *src, size_t	size)
{
	size_t i;
	size_t j;

	i = 0;
	j = 0;
	if (size == 0)
		return (i);
	while (dst[i] != '\0')
		i++;
	while (src[j] != '\0' && j < size - 1)
	{
		dst[i + j] = src[j];
		j++;
	}
	dst[j] = '\0';
	return (i);
}