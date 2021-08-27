def func(n):

    coins = n
    ans = 0

    if n % 2 == 1:
        return n - func(n-1)

    else:
        while(coins > 0):
            if coins == 4:
                ans += 3
                coins -= 4
            elif coins % 4 == 0:
                ans += 1
                coins -= 2
            else:
                ans += coins//2
                coins -= (coins//2 + 1)

    return ans

if __name__ == '__main__':
    t = int(input())
    ns = []
    for i in range(t):
        ns.append(int(input()))

    for n in ns:
        print(func(n))

'''
6
1
2
5
6
12
1000000000000000000

1
1000000000000000000
'''