def func(n, k):
    arr = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        arr[i][0] = 1

    for i in range(n):
        for j in range(1, i+2):
            arr[i+1][j] = arr[i][j] + arr[i][j-1]

    return arr



if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = func(n, k)

    for line in arr:
        for val in line:
            print("%4d" %(val), end="")
        print()