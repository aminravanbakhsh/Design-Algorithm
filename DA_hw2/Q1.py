def func(As, i, An, k, val, count):
    if i == An:
        # print('\n', val, end=' ')
        if val % k == 0:
            # print('Ture', end='')
            count[0] += 1
    else:
        for w in As[i]:
            func(As, i+1, An, k, val + w, count)

def main():
    n, k = map(int, input().split())
    ws = []
    for i in range(n):
        ws.append(int(input()))

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
        As.append([key * i for i in range(w_dic[key] + 1)])

    count = [0]
    An = len(keys)
    func(As, 0, An, k, 0, count)
    print(count[0])

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