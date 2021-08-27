xdir = [2, 1, -1, -2, -2, -1, 1, 2]
ydir = [1, 2, 2, 1, -1, -2, -2, -1]

def check(x, y, map, n):

    if (0 <= x and x < n and 0 <= y and y < n and map[x][y] == -1):
        return True

    return False

def printMap(Map):
    for line in Map:
        for val in line:
            print(val, end=" ")
        print()

def func(x, y, q, map, n):

    if q == n*n - 1:
        map[x][y] = q
        return True

    else:
        map[x][y] = q
        for i in range(8):
            xn = x + xdir[i]
            yn = y + ydir[i]
            if check(xn,yn, map, n):
                if func(xn, yn,q+1, map, n):
                    return True

                map[xn][yn] = -1

        return False


def main():
    n = int(input())
    x, y = map(int, input().split())

    Map = [[-1 for i in range(n)] for j in range(n)]
    Map
    if not func(x,y,0,Map,n):
        print("ohh no")
    else:
        printMap(Map)

if __name__ == '__main__':
    main()