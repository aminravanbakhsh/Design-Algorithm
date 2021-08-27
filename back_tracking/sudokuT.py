def check(map, x, y, val):

    x0 = int(x/3) * 3
    y0 = int(y/3) * 3

    for i in range(9):
        if map[x][i] == val:
            return False

        if map[i][y] == val:
            return False

    for i in range(3):
        for j in range(3):
            if map[x0 + i][y0 + j] == val:
                return False

    return True


def func(map, q):
    if q >= 9 * 9:
        return True

    else:
        x = int (q/9)
        y = q % 9

        if map[x][y] == 0:
            for val in range(1,10):
                if check(map, x, y, val):
                    map[x][y] = val
                    if func(map, q+1):
                        return True

            map[x][y] = 0
            return False

        else:
            if func(map, q+1):
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