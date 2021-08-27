import copy

xn = [1, -1, 0, 0, 1, 1, -1, -1]
yn = [0, 0, 1, -1, 1, -1, 1, -1]
dir_size = 8

def checkFunc(xs, ys, i, j, q, n):

    map = [[False for k in range(n)] for l in range(n)]
    for k in range(q):
        map[xs[k]][ys[k]] = True

    for k in range(dir_size):
        for z in range(n):
            x = i + xn[k]*z
            y = j + yn[k]*z
            if 0 <= x and x < n and 0 <= y and y < n:
                if map[x][y]:
                    return False

    return True

def printFunc(xs, ys, n):
    map = [['_' for k in range(n)] for l in range(n)]
    for k in range(n):
        map[xs[k]][ys[k]] = 'Q'

    for line in map:
        for val in line:
            print(val, end='')
        print()

def func(xs, ys, q, n):

    if q == n:
        return True

    else:
        for i in range(n):
            for j in range(n):


                if checkFunc(xs, ys, i, j, q, n):
                    xs[q] = i
                    ys[q] = j

                    if func(xs, ys, q+1, n):
                        return True

        xs[q] = -1
        ys[q] = -1
        return False



def main():
    n = int(input())
    xs = [-1 for i in range(n)]
    ys = [-1 for i in range(n)]
    if not func(xs, ys, 0, n):
        print('fuck this problem')

    print(xs, ys, sep='\n')
    printFunc(xs, ys, n)

if __name__ == '__main__':
    main()