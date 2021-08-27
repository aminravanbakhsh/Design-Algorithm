def func(n):

    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        arr[i][0] = 1

    for i in range(0, n-1):
        for k in range(1,i+2):
            arr[i+1][k] = (k+1) * arr[i][k] + arr[i][k-1]

    ans = 0
    for i in range(n):
        ans += arr[n-1][i]

    return ans

def main():
    n = int(input())
    print(func(n))

if __name__ == '__main__':
    main()