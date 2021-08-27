def func(ws):
    n = sum(ws)
    s = [0 for i in range(n+1)]
    temp = [0 for i in range(n+1)]
    s[0] = 1
    temp[0] = 1

    for val in ws:
        for i in range(val, n+1):
            temp[i] = s[i] + s[i - val]

        for i in range(n+1):
            s[i] = temp[i]

    return s

if __name__ == '__main__':
    ws = list(map(int, input().split()))
    ans = func(ws)
    n = len(ans)
    for i in range(n):
        print("%3d" %(i), end='')

    print()
    for val in ans:
        print("%3d" %(val), end='')