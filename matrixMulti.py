from numpy import random
from numpy import shape
"""
Creates a specified number of matrices with a specificed dimensions
Fills in matrices with random values from numpy.random.random() 

Computes the chain multiplication according to questions

"""


#using the recursive algorithm from matrix start to matrix end with dimensions d
def recursive_chain(dimensions, start, end):
	if(start == end):
		return 0
	for k in range(start, end):
		product = recursive_chain(dimensions, start, k) + recursive_chain(dimensions, k+1, end) + (dimensions[start-1] * dimensions[k]* dimensions[end])
	return product


def main():
	print("Chain Multiplying Matrices")
	num = input("Enter the number of matrices: ")
	counter = 0
	matrices = [[0 for x in range(num)] for x in range(num)] #extra row and columns of zero
	d = []
	print(matrices)
	while(counter < num):
		size = raw_input("Enter dimensions for each matrix (rows x cols): ")
		dim = size.split("x")
		d.append(int(dim[0]))
		tmp = random.randint(0 , 100, (1, int(dim[0]), int(dim[1])) ) # creates one matrix full of values between 1 and 100, with the given dimensions and adds it to the the matrices
		print(tmp)
		matrices.append(tmp)
		counter = counter + 1 
	print("\n\n")
	print("computing the optimal order and cost...")
	print("matrices with dimensions" , d)
	print((len(d) - 1))
	print("\n\n")
	print(recursive_chain(d, 1, (len(d)-1)))
	return

	
main()