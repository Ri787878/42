# 42

My part on the 42 Piscine

# Shell

- Shell 00 (50%)
- Shell 01 (0%)

# Piscine

- C 00  (50%)
- C 01  (100%)
- C 02  (65%)
- C 03  (50%)
- C 04  (50%)
- C 05  (50%)
- C 06  (tbd)


# Libft


The libft folder contains a library of custom C functions that can be used in other C programs. These functions are designed to be lightweight and efficient, and can be used to perform common tasks such as string manipulation, memory allocation, and character classification.

### Contents

The libft folder contains the following files:

- **ft_substr.c:** A function that returns a substring of a given string.
- **ft_isalpha.c:** A function that checks whether a given character is an alphabetic character.
- **ft_memset.c:** A function that sets a block of memory to a given value.

- **ft_bzero.c:** A function that sets a block of memory to zero.
- ft_memcpy.c: A function that copies a block of memory from one location to another.
- **ft_memccpy.c:** A function that copies a block of memory from one location to another until a given character is found.
- **ft_memmove.c:** A function that copies a block of memory from one location to another, handling overlapping memory blocks correctly.

- **ft_memchr.c:** A function that searches a block of memory for a given character.
- **ft_memcmp.c:** A function that compares two blocks of memory.
- **ft_strlen.c:** A function that returns the length of a given string.

- **ft_strlcpy.c:** A function that copies a string to a given buffer, ensuring that the buffer is not overrun.
- **ft_strlcat.c:** A function that concatenates two strings to a given buffer, ensuring that the buffer is not overrun.
- **ft_strchr.c:** A function that searches a string for a given character.

- **ft_strrchr.c:** A function that searches a string for a given character, starting from the end of the string.
- **ft_strncmp.c:** A function that compares two strings up to a given length.
- **ft_atoi.c:** A function that converts a string to an integer.

- **ft_isdigit.c:** A function that checks whether a given character is a digit.
- **ft_isalnum.c:** A function that checks whether a given character is an alphanumeric character.
- **ft_isascii.c:** A function that checks whether a given character is an ASCII character.

- **ft_isprint.c:** A function that checks whether a given character is a printable character.
- **ft_toupper.c:** A function that converts a given character to uppercase.
- **ft_tolower.c:** A function that converts a given character to lowercase.

### Usage

To use the functions in the libft library, include the appropriate header file in your C program:

```
#include "libft.h"
```

Then, you can call the functions as needed:

```
char *str = "Hello, world!";
int len = ft_strlen(str);
```

### License

The libft library is released under the MIT license. See the LICENSE file for more information.

### Credits

This libft library was created by Ricardo Dias.
