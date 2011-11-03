#Coding time: 85 minutes
from __future__ import print_function	# Use print as function (in Python 3.x)

def empty_square_matrix(size):
	square_matrix = []
	for i in range(size):
		square_matrix.append([0])
		for j in range(size-1):
			square_matrix[i].append(0)
	return square_matrix

def print_matrix_with_format(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{0:>4}'.format(str(matrix[i][j])), end='')
        print("")

if __name__ == '__main__':
    N = raw_input('Nhap N: ')
    N = int(N)
    spiral_matrix = empty_square_matrix(N)
    
    numb = 1
    max_layer = (N / 2) + (N % 2)
    print('Total layer = ', max_layer)
    for layer in range(max_layer):
        for i in range(layer,N-layer-1):
            spiral_matrix[layer][i] = numb
                        
            spiral_matrix[i][N-layer-1] = numb-layer + (N-layer-1)
                        
            spiral_matrix[N-layer-1][N-i-1] = numb-(2*layer) + 2*(N-layer-1)
                        
            spiral_matrix[N-i-1][layer] = numb-(3*layer) + 3*(N-layer-1)
                        
            numb += 1
            
        numb = numb-(3*layer) + 3*(N-layer-1)
        
    if N % 2 == 1: 
        spiral_matrix[N/2][N/2] = N*N   # Freak, because behavior of range() function
    
    print_matrix_with_format(spiral_matrix)