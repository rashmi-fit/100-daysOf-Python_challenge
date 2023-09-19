'''
Write a function to generate Gauss Seidel Iteration 
'''
import numpy as np
i=4
matrix=np.random.randint(-100,100,size=(i,i))
matrix
diagonal = 0

counter = 0

for j in range(len(matrix)):
    non_diagonal = 0
    for k in range(len(matrix)):
        if j == k:
            diagonal = abs(matrix[j,k])
        else:
            non_diagonal += abs(matrix[j,k])
    if diagonal >= non_diagonal:
        counter += 1
    else:
        break

if counter == len(matrix):
    print("diagonally dominant")
        
else:
    print("not digonally dominant")