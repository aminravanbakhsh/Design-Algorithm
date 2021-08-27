def getN(n_arr, p, q):
    k = len(n_arr)
    rp = k
    lp = 0
    ip = int(k/2)
    while(not(n_arr[ip] == p or rp == ip or ip == lp)):
        if n_arr[ip] < p:
            lp = ip
            ip = int((lp+rp)/2)
        else:
            rp = ip
            ip = int((lp+rp)/2)

    rq = k
    lq = 0
    iq = int(k/2)
    while(not(n_arr[iq] == q or rq == iq or iq == lq)):
        if n_arr[iq] < q:
            lq = iq
            iq = int((lq+rq)/2)
        else:
            rq = iq
            iq = int((lq+rq)/2)

    if n_arr[ip] == p:
        ip -= 1


    return iq, ip

def log(n):
    x = 0
    while (n > 1):
        n /= 2
        x += 1

    return int(x)

def func(arr,sums, p, q, A, B):

    #     one cell
    if p == q:
        iq, ip = getN(arr, p, q)
        if iq == ip:
            return A
        else:
            return B * (sums[iq] - sums[ip])

    iq, ip = getN(arr, p , q)
    l = q - p +1
    trash = sums[iq] - sums[ip]
    dirty_cells = iq - ip

    if trash == 0:
        return A

    #    one cell in array
    if dirty_cells == 1:
        minszie = A / (B * trash)
        ll = log(l)
        lm = log(minszie)

        if minszie < l:
            return A * (ll - lm) + (2**lm) * (trash * B)
        else:
            return l * trash * B


    #   more trash in array
    m = (1 + p + q) // 2
    x1 = func(arr,sums,p,m-1,A,B) + func(arr,sums,m,q,A,B)
    x2 = trash*B*l
    return min(x1, x2)

def main():
    n, k, A, B = map(int, input().split())
    arr = list(map(lambda x: int(x) - 1, input().split()))
    arr.sort()
    dic = {}
    dic[arr[0]] = 1
    for i in range(1, k):
        if arr[i] == arr[i-1]:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1

    n_arr = list(dic.keys())
    n_arr.insert(0, -1)

    vals = list(dic.values())
    vk = len(vals)

    sums = [0]
    for i in range(vk):
        sums.append(sums[i] + vals[i])

    print(int(func(n_arr, sums, 0, 2**n-1, A, B)))

if __name__ == '__main__':
    main()

'''
2 2 1 2
1 1

3 4 100 1
1 1 1 1

30 3 2 1
3 5 6

3 3 2 1
3 5 6


30 3 0 1
17 5 6

3 2 1 2
5 2


2 2 1 2
1 3

3 2 1 2
1 7

3 2 1 2
1 7
2 8

3 8 1 2
1 2 3 4 5 6 7 8

6 8 1 2
3 11 19 27 35 43 51 59
'''