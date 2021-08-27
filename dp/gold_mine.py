def func(map, n, path):
    arr = [[0 for i in range(n)] for j in range(n)]
    path = [[[] for i in range(n)] for j in range(n)]

    for i in range(n):
        arr[i][0] = map[i][0]
        path[i][0] = [i, -1]

    for i in range(1, n):
        for j in range(n):
            for k in range(-1, 2):
                y = j + k
                if 0 <= y and y < n:
                    z = arr[y][i-1] + map[j][i]
                    if arr[j][i] < z:
                        arr[j][i] = z
                        path[j][i] = [y, i-1]

    x = n-1
    y = -1
    ans = 0
    for i in range(n):
        if ans < arr[i][n-1]:
            ans = arr[i][n-1]
            y = i

    way = [[y, x]]
    for i in range(n-1):
        x0 = path[y][x][1]
        y0 = path[y][x][0]
        way.append([y0,x0])
        x = x0
        y = y0

    return ans, way


def main():
    n = int(input())
    Map = []
    path = [[[] for i in range(n)] for j in range(n)]
    for i in range(n):
        Map.append(list(map(int, input().split())))

    ans, way = func(Map, n, path)
    print(ans)
    way.reverse()
    for val in way:
        print(val[1], val[0], end="\n")

if __name__ == '__main__':
    main()