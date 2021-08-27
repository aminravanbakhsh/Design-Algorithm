def func(A, k):
    n = len(A)
    dp = [[1 for j in range(k+1)] for i in range(n)]

    for i in range(n):
        for j in range(k+1):
            for l in range(j+1):
                x = j - l
                y = i - l - 1
                if y >= 0:
                    if A[i] >= A[y]:
                        dp[i][j] = max(dp[i][j], dp[y][x] + 1)

    ans = 0
    for i in range(n):
        for j in range(k+1):
            if dp[i][j] > ans:
                ans = dp[i][j]

    return ans

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(func(arr, k))

if __name__ == '__main__':
    main()

'''

8 2
2 3 8 4 5 5 7 6


5 2
5 2 3 1 4

13 1
38 13 1 21 36 14 12 38 35 17 10 16 8

7 1
1 8 9 2 3 4 5

'''

'''
i = indxe arr
idx = len correct
j = count of k
p_index[i]

k_prime = i - p_index - idx - 1
'''