import numpy as np

def gram_schmidt(A):
    matrix = A.T.tolist()
    qs = []

    for val in matrix:
        q = np.array(val)
        for vec in qs:
            q -= np.dot(vec, q)*vec

        q = q / np.linalg.norm(q)
        qs.append(q)


    return np.array(qs)

if __name__ == '__main__':
    print("enter m and n:")
    m, n = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(float, input().split())))

    A = np.array(A)
    print(gram_schmidt(A))

'''    
3 3
1 2 2
2 1 2
2 2 1

3 3
2 1 3
0 2 4
0 0 5

3 3
2 0 0
1 2 0
3 4 5

3 4
1 2 2 2
2 4 5 5
2 1 2 3


'''