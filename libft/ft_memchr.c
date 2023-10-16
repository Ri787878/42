#include "libft.h"

void	*ft_memchr( const void *ptr, int ch, size_t count )
{
	unsigned long int	i;

	i = 0;
	while(i < count)
	{
		if (((unsigned char *)ptr)[i] == (unsigned char)ch)
			return ((void *)ptr + i);
		i++;
	}
	return (NULL);
}