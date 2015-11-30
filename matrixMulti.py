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
		size = raw_input("Enter dimensions for each matrix (rows x cols): ")
		dim = size.split("x")
		tmp = random.randint(0 , 100, (1, int(dim[0]), int(dim[1])) ) # creates one matrix full of values between 1 and 100, with the given dimensions and adds it to the the matrices
		print(tmp)
		matrices.append(tmp)
		counter = counter + 1 
		
	print(matrices)
	return
	
	
main()