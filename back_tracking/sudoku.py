mapSize = 9

def checkFunc(map, x, y, val):

    for i in range(mapSize):
        if map[x][i] == val:
            return False

    for i in range(mapSize):
        if map[i][y] == val:
            return False

    xo = int(x/3) * 3
    yo = int(y/3) * 3

    for i in range(3):
        for j in range(3):
            if map[xo + i][yo + j] == val:
                return False

    return True

def func(map, q):
    if q == 9*9:
        return True

    j = q % 9
    i = int(q/9)
    if map[i][j] == 0:
        for val in range(1,10):
            if checkFunc(map, i, j, val):
                map[i][j] = val
                if func(map, q+1):
                    return True

        map[i][j] = 0
        return False

    else:
        if func(map, q + 1):
            return True
        return False

def printFunc(arr):
    for line in arr:
        for val in line:
            print(val, end=" ")
        print()

def main():
    arr = []

    for i in range(9):
        line = list(map(int, input().split()))
        arr.append(line)

    if not func(arr, 0):
        print("ooh no, this is wrong")
    else:
        printFunc(arr)

if __name__ == '__main__':
    main()