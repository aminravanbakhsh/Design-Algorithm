import copy

def func(ws):
    n = sum(ws)
    s = [0 for i in range(n+1)]
    arrs = [[] for i in range(n+1)]
    s[0] = 1
    arrs[0] = [[]]


    for val in ws:
        s_temp = copy.deepcopy(s)
        arrs_temp = copy.deepcopy(arrs)
        for i in range(val, n+1):
            s_temp[i] = s[i - val] + s[i]
            if s_temp[i] > 0:
                for arr in arrs[i-val]:
                    x = copy.deepcopy(arr)
                    x.append(val)
                    arrs_temp[i].append(x)

        s = copy.deepcopy(s_temp)
        arrs = copy.deepcopy(arrs_temp)

    return s, arrs

if __name__ == '__main__':
    ws = list(map(int, input().split()))
    s , arrs = func(ws)
    n = len(s)

    for i in range(n):
        print("%3d, s = %3d: " %(i, s[i]), end=" ")
        for val in arrs[i]:
            print(val , end=" , ")

        print()