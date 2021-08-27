import copy

def recursion(ws, m, total, code, codes):

    if m < 0 or total < 0:
        return

    if total == 0:
        codes.append(code)
        return

    x = copy.deepcopy(code)
    x.append(ws[m-1])
    recursion(ws, m-1, total - ws[m-1], x, codes)

    recursion(ws, m-1, total, code, codes)

def func(ws, total):
    n = len(ws)
    codes = []
    recursion(ws, n, total, [], codes)

    return codes

if __name__ == '__main__':
    ws = list(map(int, input().split()))
    total = int(input())

    print(func(ws, total))
