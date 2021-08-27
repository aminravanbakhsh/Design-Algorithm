import numpy as np
import copy as cp

def gauss_seidel(A):
    shape = A.shape
    m = shape[0]
    n = shape[1]

    k = min(n, m)
    ps = []
    ls = []
    es = []
    U = cp.deepcopy(A)

    for i in range(k):
        e = np.eye(k)
        u = np.eye(k)
        l = np.eye(k)

        check = False
        for j in range(i, m):
            if U[j][i] != 0:
                check = True
                e[[i, j]] = e[[j, i]]
                U = np.dot(e, U)
                es.append(e)
                break

        if check:
            for j in range(i+1, m):
                u[j][i] = - U[j][i] / U[i][i]
                l[j][i] = U[j][i] / U[i][i]

        U = np.dot(u, U)
        ps.append(u)
        ls.append(l)

    size_ls = len(ls)
    L = np.eye(k)
    E = np.eye(k)
    for i in range(size_ls-1, -1, -1):
        L = np.dot(ls[i], L)

    size_es = len(es)
    for i in range(size_es-1,-1, -1):
        E = np.dot(es[i], E)

    return L, U, E

if __name__ == '__main__':

    print("enter m and n:")
    m, n = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(float, input().split())))

    A = np.array(A)
    L, U, E = gauss_seidel(A)
    print(L)
    print(U)
    print(E)
    print(np.dot(L, U))


'''
3 3
1 2 2
2 1 2
2 2 1

3 3
1 2 2
2 4 5
2 1 2

3 4
1 2 2 2
2 4 5 5
2 1 2 3

4 5
1 2 1 3 2
2 4 1 5 3
3 6 1 7 1
4 8 1 9 4

'''