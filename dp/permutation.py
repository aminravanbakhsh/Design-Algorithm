def func(n, k):
    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        arr[i][0] = i+1

    for i in range(n-1):
        for j in range(1, i+2):
            arr[i+1][j] = (j+1) * arr[i][j-1] + arr[i][j]

    return arr[n-1][k-1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(func(n, k))