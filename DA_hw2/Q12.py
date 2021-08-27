import numpy as np

def func(ws, k):

    s = sum(ws)

    w_dic = {}
    for w in ws:
        if w_dic.__contains__(w):
            w_dic[w] += 1
        else:
            w_dic[w] = 1

    keys = list(w_dic.keys())
    As = []
    for key in keys:
        As.append([key * (i + 1) for i in range(w_dic[key])])

    dp =  np.zeros((s+1))
    dp[0] = 1

    for A in As:
        dp_prime = np.zeros((s+1))
        for w in A:
            for i in range(s+1 - w):
                dp_prime[i + w] += dp[i]

        dp += dp_prime

    z = s // k
    ans = 0
    for i in range(z+1):
        ans += dp[i * k]

    return int(ans)

def main():
    n, k = map(int, input().split())
    ws = []
    for i in range(n):
        ws.append(int(input()))

    print(func(ws, k))

if __name__ == '__main__':
    main()

'''
5 4 
5
3
6
3
5

4 2
1
2
3
4

10 1
13
13
26
78
312
1560
9360
65520
524160
4717440

9 1
13
26
78
312
1560
9360
65520
524160
4717440

'''