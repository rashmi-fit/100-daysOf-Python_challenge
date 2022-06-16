import numpy as np

# import solve

i=4
A=np.random.randint(-100,100,size=(i,i))

def GaussSeidel(A,B,x,n):
    L=np.tril(A)
    U=A-L
    for i in range(n):
        x=np.dot(np.linalg.inv(L),B-np.dot(U-x))
        print(x)
    return x