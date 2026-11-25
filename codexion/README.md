### Error Codes:

	- Argument parsing errors reported to stderr return '-20'.
	- '-30' to '-39' are Memory errors:
		- '-30' Expected variable to not be 'NULL', but 'NULL';
		- '-31' Error allocating dongles or coders array;
	- '-40' to '-49' are Validation errors:
		- '-40' Number of coders must be more than 0;
		- '-41' Number of compiles must be more than 0;
		- '-42' Number of time_to_burnout of  must be more 0;
		- '-43' Number of time_to_compile must be more than 0;
		- '-44' Number of time_to_debug must be more than 0;
		- '-45' Number of time_to_refactor must be more than 0;
		- '-46' Number of dongle_cooldown must be more than 0;

## Schedulers
### FIFO
FIFO selects waiting compile requests in arrival order.
### EDF
EDF selects the waiting coder with the earliest deadline for the next compile. The deadline is `last_compile_start + time_to_burnout`; ties use request arrival order.

## Coder Work Cycle
A coder acquires both adjacent dongles only to compile. After a successful compile, if it has not reached its required compile count, it debugs and then refactors before requesting another compile. Debugging and refactoring do not use dongles and may overlap with other coders' work.

## Stop Conditions
The simulation stops once one of the following is reached:
	- Each coder reaches the required amount of compiles;
	- A coder burns out;


### Dongle Cooldown
A dongle’s cooldown starts at 0 and is applied after its used.

# References:
	- https://man7.org/linux/man-pages/man3/pthread_create.3.html
	- https://www.geeksforgeeks.org/c/multithreading-in-c/
	- https://www.geeksforgeeks.org/c/thread-functions-in-c-c/
	- https://linuxhint.com/gettimeofday_c_language/
	- https://stackoverflow.com/questions/19324306/running-two-threads-at-the-same-time
	-
	-
	-
