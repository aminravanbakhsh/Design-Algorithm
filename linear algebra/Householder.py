import numpy as np
import copy as cp

def getH(V):
    n = len(V)
    e = np.zeros((n,n))
    e[0] = V
    e = np.dot(e.T, e)/(0.5 * np.dot(V, V))
    return (np.eye(n) - e)

def QR(A):
    U = A.T
    qs = []
    rs = []
    n = len(A)
    for i in range(n):


if __name__ == '__main__':
    pass