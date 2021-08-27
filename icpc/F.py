def check(arr, j, n, m, k):
    x = m
    y = k
    for i in range(j, n):
        if m < 0:
            return False

        if y - arr[i] < 0:
            x -= 1
            y = k

        y -= arr[i]

    if x > 0:
        return True

    return False

def find(arr, n, m, k):

    l = 0
    r = n-1
    while(r>l):
        q = (r + l)//2
        if check(arr, q, n, m, k):
            r = q
        else:
            l = q+1

    return r

def main():
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(n - find(arr, n, m, k))

if __name__ == '__main__':
    main()


'''
5 2 6
5 2 1 4 2

5 1 4
4 2 3 4 1

'''