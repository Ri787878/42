*This project has been created as part of the 42 curriculum by ridias.*

# push_swap

## Description
This project attempts intends to teach us (the students), about diferent sorting algorithms and their associated costs. The objective it self is pretty simple, organize a stack of numbers given as an input while using a set number of permitted movements.

The diferent types of movements are:
- `sa` (swap a): Swap the first 2 elements at the top of stack `a`.  
  Do nothing if there is only one element or none.
- `sb` (swap b): Swap the first 2 elements at the top of stack `b`.  
  Do nothing if there is only one element or none.
- `ss`: `sa` and `sb` at the same time.
- `pa` (push a): Take the first element at the top of `b` and put it at the top of `a`.  
  Do nothing if `b` is empty.
- `pb` (push b): Take the first element at the top of `a` and put it at the top of `b`.  
  Do nothing if `a` is empty.
- `ra` (rotate a): Shift up all elements of stack `a` by 1.  
  The first element becomes the last one.
- `rb` (rotate b): Shift up all elements of stack `b` by 1.  
  The first element becomes the last one.
- `rr`: `ra` and `rb` at the same time.
- `rra` (reverse rotate a): Shift down all elements of stack `a` by 1.  
  The last element becomes the first one.
- `rrb` (reverse rotate b): Shift down all elements of stack `b` by 1.  
  The last element becomes the first one.
- `rrr`: `rra` and `rrb` at the same time.

### Algorithm
The Algorithm used in this project was Radix sort, using an indexing trick to minimize the cost of operations aswell as allowing the program to also sort negative numbers.

### Normal functioning
The program works by first checking for known errors such as: repetitive numbers, non-numbers being given as an input, empty strings, etc.. 
After this first step the program converts the given numbers to be stored inside a linke list, where they are used later on for the sorting part of the program. Next the program uses the trick of indexting, to permit the program to sort negative numbers. this works by inserting the numbers into a array of ints, where they are sorted. It is after the array is sorted that the program saves the index of each number in a special variable associated with the number, this is the number that allows the program to binary sort the numbers without needing to worry about negative numbers. 
The binary sort works by procedurally compare each bit to check if they are 1 or 0 and respectively rotating them or pushing them to the other stack, this way we are able to sort the numbers not by their actual number but bit by bit of their composition. 
Finally the program frees both stacks and exits the program.

### Special cases
This program uses a special simpler version to sort the numbers if the number of arguments is either 3, 4 or 5. Simply checking if it is sorted in the case of 2 numbers, and swaping them if they arent sorted.

PS: When doing each movement the program prints the movement made.

## Instructions

```
$ make
$ cc -Wall -Wextra -Werror push_swap.a -o push_swap
$ ./push_swap <the numbers you want to organize>
```

## Resources

-	<https://www.geeksforgeeks.org/c/doubly-linked-list-in-c/>
-	<https://www.geeksforgeeks.org/dsa/radix-sort/>
-	<https://www.geeksforgeeks.org/dsa/sorting-algorithms/>
-	<http://games.hazzens.com/blog/2014/02/27/turk_sort.html>

The use if AI in this project revolved mostly around optimizing or getting a diferent perspective on how to organize some functions. And also to better understand the indexing part of the algorithm.