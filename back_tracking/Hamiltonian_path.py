def check(map, pathCheck, q, paths, n):
    check = False

    if pathCheck[q]:
        return False

    for i in range(n):
        if map[q][i] == 1:
            if not pathCheck[i]:
                paths.append(i)
                check = True

    return check

def func(map, arr, idx, q, seenArr, n):

    if idx == n-1 and map[q][0] == 1:
        arr[idx] = q
        seenArr[q] = True
        return True

    else:
        paths = []
        if check(map,seenArr, q, paths, n):
            arr[idx] = q
            seenArr[q] = True

            for val in paths:
                if func(map, arr, idx+1, val, seenArr, n):
                    return True

            arr[idx] = -1
            seenArr[q] = False

        return False

def main():
    n = int(input())
    Map = []
    for i in range(n):
        Map.append(list(map(int, input().split())))

    seenArr = [False for i in range(n)]
    arr = [-1 for i in range(n)]
    if not func(Map, arr, 0, 0, seenArr, n):
        print("ohh no")
    else:
        for val in arr:
            print(val, end=" ")
        print('0')

if __name__ == '__main__':
    main()