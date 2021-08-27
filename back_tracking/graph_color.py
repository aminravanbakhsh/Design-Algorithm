def check(map, arr, idx, val, n):

    if map[idx][idx] == 1:
        return False

    for i in range(n):
        if map[idx][i] == 1:
            if arr[i] == val:
                return False

    return True

def func(map, arr, idx, m, n):

    if idx == n:
        return True

    else:
        for val in range(1, m+1):
            if check(map, arr, idx, val, n):
                arr[idx] = val
                if func(map, arr, idx+1, m, n):
                    return True
                else:
                    arr[idx] = [0]

        return False

def main():
    m = int(input())
    n = int(input())
    Map = []
    for i in range(n):
        Map.append(list(map(int, input().split())))

    arr = [0 for i in range(n)]

    if not func(Map, arr, 0, m, n):
        print("ohh no")

    else:
        print(arr)


if __name__ == '__main__':
    main()