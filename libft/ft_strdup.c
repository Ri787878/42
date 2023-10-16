#include "libft.h"

char * ft_strdup( const char *str1 )
{
	char *dupped;
	int leng;

	leng = 0;
	while(str1[leng] != '\0')
	{
		leng++;
	}
	if(str1)
	{
		dupped = ft_calloc(leng + 1, 1);
		leng = 0;
		while(str1[leng] != '\0')
		{
			dupped[leng] = str1[leng];
			leng++;
		}
	}
	return (dupped);
}