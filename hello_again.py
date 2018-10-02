#include the Numpy library
import numpy as np

#define the main () function
#everything that is under a main function it should be indented
def main(): 

	i = 0		#declare an integer i, set to 0, can also be negative
	x = 119.0	#declare a float x, with val 119, is a number that can have fractional components 
	
	for i in range(120):	#loops i from 0 through 119
		if((i%2)==0):	#if i is even
			x += 3.0		#add 3 to x
		else:			#if i is odd
			x -= 5.0		#x = x-5
	
	s = "%3.2e" % x			#3 values, 2 after the decimal, e signifies scientific notation  
							#makes a string that shows x with scientific notation
	
	print (s)
	
#now the rest of the program 


if __name__ == "__main__":
	main()
	
#continue 