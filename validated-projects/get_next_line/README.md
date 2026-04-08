*This project has been created as part of the 42 curriculum by ridias.*

# Get_Next_Line
This project intends to create a function capable of reading a file descriptor until a certain stop signal is reached, that being in this case a "\n", also known as a new line character.

## Algorithm and Data Structure
To write this function it is necessary to understand the need for a certain type of variables as known as "static variables". These types of variables are capable of keeping their value between multiple function calls.
This function was made to first check for remaining values in the static variable, meaning if there are leftover data from previous function calls, before reading the file descriptor.
.
## Instructions
To compile and run this project you need, for example, a file to use the function on. After that you need to add the function to your project and run the following commmands on the project directory:

```
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include "get_next_line.h"

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return 1;
    }

    int fd = open(argv[1], O_RDONLY);
    if (fd < 0)
    {
        perror("open");
        return 1;
    }

    char *line;
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);   /* line already includes the newline if present */
        free(line);
    }

    close(fd);
    return 0;
}
```

```
$ make
$ cc <your_file.c> get_next_line.c get_next_line_utils.c get_next_line.h -o ./result
$ ./result
```

## Resources

-	https://www.geeksforgeeks.org/c/g-fact-80/
-	https://www.geeksforgeeks.org/c/static-variables-in-c/
-	https://github.com/megyant
