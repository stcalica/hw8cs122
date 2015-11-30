from numpy import random
"""
Creates a specified number of matrices with a specificed dimensions
Fills in matrices with random values from numpy.random.random() 

Computes the chain multiplication according to questions

"""

def main():
	print("Chain Multiplying Matrices")
	num = input("Enter the number of matrices: ")
	counter = 0
	matrices = [] 
	while(counter < num):
		size = str(input("Enter dimensions for each matrix (m x n): "))
		dim = size.split("x")
		print(dim)
		
	
	return
	
	
main()