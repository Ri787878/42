*This project has been created as part of the 42 curriculum by ridias.*

# Ft_printf
This project attempts to recreate a simplified version of the printf function from libc.
The porpose of this function is to print a string, that could be or not interspaced with diferent variables of diferent types.

Types of variables handled by the function:

1. %c - single char
2. %s - string
3. %p - void * (a pointer)
4. %d - decimal (base 10) number
5. %i - interger (base 10)
6. %u - unsigned decimal (base 10)
7. %x - number in hexadecimal (lowercase)
8. %X - number in hexadecimal (uppercase)
9. %% - prints the "%" char

## Algorithm and Data Structure
To complete this project I choose to use variadic functions for it's ability to receive anon specified amount of variables and store them on a FIFO list. 

## Instructions
To compile and run this project run the following commmands on the project directory:

```
$ make
$ cc <your_file.c> libftprintf.a  -o ./result
$ ./result
```

## Resources

https://www.geeksforgeeks.org/c/variadic-functions-in-c/
https://linux.die.net/man/3/printf
https://www.geeksforgeeks.org/c/printf-in-c/

