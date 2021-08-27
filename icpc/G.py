import copy
import numpy as np

def func(arr):
    sum_arr = sum(arr)
    n = len(arr)

    dp = [0 for i in range(sum_arr+1)]
    dp[0] = 1
    for i in range(n):
        dp_prime = [0 for i in range(sum_arr+1)]
        for k in range(sum_arr+1 - arr[i]):
            dp_prime[k + arr[i]] = dp[k]

        dp = np.add(dp, dp_prime)

    print(dp)

def main():
    As = list(map(int, input().split()))
    arr = []
    for i in range(10):
        s = 0
        for j in range(As[i]):
            s += i
            arr.append(s)

    func(arr)


if __name__ == '__main__':
    main()

'''
0 2 1 0 0 0 0 0 0 0

'''