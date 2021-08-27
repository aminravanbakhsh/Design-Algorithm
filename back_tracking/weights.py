import numpy as np

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sumT = sum(arr)

    k = 2**n
    bestVal = 100000000000
    bestArr = []

    for i in range(k):
        ans = 0
        checkArr = []

        x = i
        q = 0
        while (x > 0):
            if x % 2 == 1:
                checkArr.append(q)
                ans += arr[q]

            x = int(x/2)
            q += 1

        ans = np.abs(sumT - 2 * ans)
        if ans < bestVal:
            bestVal = ans
            bestArr = checkArr

    print(bestVal)
    print("b:", bestArr)


if __name__ == '__main__':
    main()