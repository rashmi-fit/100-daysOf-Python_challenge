import numpy as np

A=np.array([[ 40., 7.,   5.],
               [ 5., 90.,  7.],
               [20., 7., 50.]])

def dd(X):
    D = np.diag(np.abs(X)) # Find diagonal coefficients
    S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        print('matrix is diagonally dominant')
    else:
        print('NOT diagonally dominant')
    return

dd(A)

