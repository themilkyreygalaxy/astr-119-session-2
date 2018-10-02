import numpy as np	#we use numpy for lots o' things

def main():
	i = 0			#declare i equal to 0
	n = 10 			#declare n equal to 10
	x = 119.0		#float x, these have a . (period)
	
	#we can use numpy to quickly make array
	y = np.zeros(n,dtype=float) #declares 10 zeros as floats using numpy
	
	#we can use for loops to iterate through a variable
	for i in range(n):	#i in range [0,n-1] or basically [0,1,2,3,4,5,6,7,8,9]
		y[i] = 2.0 * float(i) + 1.0 #set y = 2i +1 as floats
		
	#we can iterate through the y elements one by one
	for y_element in y: 
		print (y_element)
		
#execute the main function

if __name__ == "__main__":
	main()