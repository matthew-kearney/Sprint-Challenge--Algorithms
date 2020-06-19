#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
0(n) 
because n is run only once in the while loop and a is given an already saved value of n.
run time increases linearly as n increases. Single loop.




b) 
O(n^2)
the code goes through the first iteration and then has to run a while loop, making it the second iteration of it running n
2 loops So run time increases twice as n increases. 



c)
0(log n)
the runtime will increase at a constant pace with the size of the input.

## Exercise II
binary search

suppose you drop the egg from the middle floor, if the comes back as is egg broke, go to the current floor - 1 and try again until it says back the egg not broken

then if the return value from the middle floor is egg not broken, go to the current floor + 1 until you get back the is egg broken

when you get the return to be egg broken then move to the current floor - 1 and return it


it would be a 0(log n) runtime complexcity 
