#!/bin/bash
make re
make clean

#clear

echo "cc -Wall -Wextra -Werror push_swap.a -o test"
cc -Wall -Wextra -Werror push_swap.a -o test
echo "./test \"3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4\""
./test 3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4

#echo "valgrind  --leak-check=full ./test \"3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4\""
#valgrind  --leak-check=full ./test "3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4"
