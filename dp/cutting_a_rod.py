import copy

def func(n, table = {}):
    ws = list(table.keys())
    s = [0 for i in range(n+1)]

    for val in ws:
        if val <= n:
            for i in range(n-val, -1, -1):
                x = table[val] + s[i + val]
                if x > s[i]:
                    s[i] = x

    return s[0]


if __name__ == '__main__':
    n = int(input())
    table = {}
    m = int(input())
    for i in range(m):
        size, price = map(int, input().split())
        table[size] = price

    print(func(n, table))

'''
2
3
1 3
2 4
4 8


8
8
1 2
2 5
3 8
4 9
5 10
6 17
7 17
8 20


'''