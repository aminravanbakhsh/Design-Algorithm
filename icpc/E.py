def func(arr, k):
    n = len(arr)
    dp = [[0 for i in range(k)] for j in range(n)]

    oa = ord('A')
    z = ord(arr[0]) - oa
    for i in range(k):
        dp[0][i] = 1
    dp[0][z] = 0

    for i in range(1, n):
        f = ord(arr[i]) - oa
        # min_val = min(dp[i-1])
        for j in range(k):
            add_val = 1
            if j == f:
                add_val = 0

            # if min_val == dp[i-1][j]:
            min_val = float('inf')
            for z in range(j):
                min_val = min(min_val, dp[i-1][z])

            for z in range(j+1, k):
                min_val = min(min_val, dp[i-1][z])

            dp[i][j] = min_val + add_val

    # for line in dp:
    #     print(line)
    return min(dp[n-1])

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = input()
    print(func(arr, k))


'''
6 3
ACCABB

6 2
AAAAAA

3 2
BBA

4 2
ABBA

'''