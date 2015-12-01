from numpy import random
from numpy import shape
import sys
import time 
MAX = sys.maxint
"""
Creates a specified number of matrices with a specificed dimensions
Fills in matrices with random values from numpy.random.random() 

Computes the chain multiplication according to questions

"""

def dynamic_chain(dimensions):
    n = len(dimensions)-1
    m, pos = {}, {}
    for i in range(1, n+1):
        m[i, i] = 0
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i,j] = MAX
            for k in range(i, j):
                product = m[i,k]+m[k+1,j]+dimensions[i-1]*dimensions[k]*dimensions[j]
                if product < m[i,j]:
                    m[i,j] = product
                    pos[i,j] = k
    return product




def memo_chain(dimensions):
	n = len(dimensions) - 1
	m = {}
	for i in range(1, len(dimensions)):
		for j in range(i, len(dimensions)):
			m[i,j] = MAX
			#print(i)
			#print(j)
			#print(m[i,j])
	#product =
	return lookup_chain(m, dimensions, 1, n)

def lookup_chain(m, dimensions, i, j):
	if(m[i,j] < 0):
		return m[i,j]
	if(i == j):
		m[i,j] = 0
		product = 0
	else:	
		for k in range(i, j):
			product = lookup_chain(m, dimensions, i, k) + lookup_chain(m, dimensions, k+1, j) + (dimensions[i-1] * dimensions[k]* dimensions[j])
			if product < m[i, j]:
				m[i,j] = product
	return product
	



#using the recursive algorithm from matrix start to matrix end with dimensions d
def recursive_chain(dimensions, start, end):
	if(start == end):
		return 0
	for k in range(start, end):
		product = recursive_chain(dimensions, start, k) + recursive_chain(dimensions, k+1, end) + (dimensions[start-1] * dimensions[k]* dimensions[end])
	return product


def main():
	print("Chain Multiplying Matrices")
	#uin = raw_input("Enter the matrix dimensions with spaces in between: ")
	#dim = []
	#uin = uin.split(" ") 
	#or d in uin:
	#	dim.append(int(d))
	dim = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 , 16, 17, 18, 19, 20, 21, 22] #, 23, 24, 25 ]
	print("\n\n")
	print("computing the optimal order and cost of a matrix with input as %i..." % len(dim))
	print("\n\n")
	
	print("Using recursion: ")
	start = time.time() 
	print(recursive_chain(dim, 1, (len(dim)-1)))
	end = time.time()
	print("Recursion took: %i minutes" % ((end-start)%60))
	
	
	print("Using memoization: ")
	start = time.time() 
	print(memo_chain(dim))
	end = time.time()
	print("Recursion took: %i minutes" % ((end-start)%60))
	
		
	print("Using DP: ")
	start = time.time() 
	print(dynamic_chain(dim))
	end = time.time()
	print("Dynamic Programming took: %i minutes" % ((end-start)%60))
	
	
	
	return

	
main()