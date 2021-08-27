def check(map, x, y, n):
    dirx = [1,-1,0,0,1,1,-1,-1]
    diry = [0,0,1,-1,1,-1,1,-1]

    for k in range(8):
        for i in range(n):
            xn = x + dirx[k]*i
            yn = y + diry[k]*i
            if 0 <= xn and xn < n and 0 <= yn and yn < n:
                if map[x + dirx[k]*i][y + diry[k]*i] == 'Q':
                    return False

            else:
                break

    return True

def func(map, q, n):
    if q == n:
        return True

    else:
        for i in range(n):
            for j in range(n):
                if check(map, i, j, n):
                    map[i][j] = 'Q'
                    if func(map, q+1, n):
                        return True

                    map[i][j] = '_'

        return False


def main():
    n = int(input())

    map = [['_' for i in range(n)] for j in range(n)]
    if not func(map, 0, n):
        print("ooh no")

    else:
        for line in map:
            for val in line:
                print(val, end = '')
            print()

if __name__ == '__main__':
    main()