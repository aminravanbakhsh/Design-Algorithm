def canGo(map, wayMap, x, y, n, dirs):
    xdir = [1,-1,0,0]
    ydir = [0,0,1,-1]
    check = False

    for i in range(4):
        xn = x + xdir[i]
        yn = y + ydir[i]
        if 0 <= xn and xn < n and 0 <= y and y < n:
            if map[xn][yn] == 1 and wayMap[xn][yn] == False:
                check = True
                dirs.append([xdir[i], ydir[i]])

    return check


def func(map, x, y, xd, yd, way, n):

    way[x][y] = True
    if x == xd and y == yd:
        return True

    dirs = []
    if canGo(map, way, x, y, n, dirs):
        for val in dirs:
            if func(map,x + val[0], y + val[1], xd, yd, way, n):
                return True

        way[x][y] = False
        return False

def main():
    n = int(input())
    Map = []
    for i in range(n):
        Map.append(list(map(int, input().split())))

    way = [[False for i in range(n)] for j in range(n)]

    if not func(Map, 0,0,n-1,n-1, way, n):
        print("ohh no")
    else:
        for line in way:
            for val in line:
                if val:
                    print("1", end = " ")
                else:
                    print("0", end = " ")

            print()

if __name__ == '__main__':
    main()