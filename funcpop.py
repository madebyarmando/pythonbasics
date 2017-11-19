
# Purpose: To showcase work with functions and calling 
# the functions in the main.


from math import *

def main(): 
	
	for t in range (-6, 7):
		print(t, end=" ")
		
		pop1(t)
				
		
	
	total = 0
	
	for t in range (-6, 7):
	
		result = pop2(t)
		
		
		total += result			
	
	print(t , result)
	print()
	print("The total is", total)
		

def pop1(t):

	pop_eq = 1 / (1 +  (e ** (-1 * t))) 

	print(pop_eq)
	

def pop2(t):

	pop_eq = 1 / (1 + (e ** (-1 * t))) 


	return pop_eq


main()



#                           ANSWER
# pop1 was not able to calculate the results due to the function not returning 
# the value of the population growth assigned to the variable pop_eq
