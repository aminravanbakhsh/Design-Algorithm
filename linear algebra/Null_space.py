import numpy as np
import copy as cp

def column_space(A):
    shape = A.shape
    m, n = shape[0], shape[1]

    U = cp.deepcopy(A)

    idx = 0
    for i in range(n):
        e = np.eye(m)
        check = False
        for j in range(idx, m):
            if U[j][i] != 0:
                check = True
                e[[idx, j]] = e[[j, idx]]
                U = np.dot(e, U)
                break

        if check:
            U[idx] = 1/U[idx][i] * U[idx]
            for j in range(idx+1, m):
                U[j] = -U[j][i]*U[idx] + U[j]

            idx += 1


    pivots = []
    idx = 0
    for i in range(n):
         if U[idx][i] == 1:
             pivots.append(i)
             for j in range(idx-1, -1, -1):
                 U[j] = -U[j][i]*U[idx] + U[j]

             idx += 1


    free = list(set(range(n)) - set(pivots))

    F = []
    for idx in free:
        F.append(U[:,idx])

    F = np.array(F)
    F = F.T

    col = []
    col.extend((-1*F[:len(pivots)]).tolist())
    col.extend(np.eye(len(free)).tolist())

    e = np.eye(n)
    idxs = cp.deepcopy(pivots)
    idxs.extend(free)
    E = []
    for i in range(n):
        E.append(e[idxs[i]])

    E = np.array(E)
    E = E.T

    return U, np.dot(E,col)

if __name__ == '__main__':
    print("enter m and n:")
    m, n = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(float, input().split())))

    A = np.array(A)
    U, F = column_space(A)
    print(U)
    print(F)