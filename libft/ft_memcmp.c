#include "libft.h"

int ft_memcmp( const void* w1, const void* w2, size_t count )
{
	size_t	i;

	i = 0;
	while (i < count)
	{
		if(((unsigned char *)w1)[i] != ((unsigned char *)w2)[i])
			return (((unsigned char *)w1)[i] - ((unsigned char *)w2)[i]);
		i++;
	}
		return (((unsigned char *)w1)[i] - ((unsigned char *)w2)[i]);
}
