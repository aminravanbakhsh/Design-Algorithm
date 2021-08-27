def func(n):
    fac = [1]
    for i in range(1, n+1):
        fac.append(fac[i-1] * i)

    m_min = int(n/2)
    twoPow = [1]
    for i in range(1, m_min + 1):
        twoPow.append(twoPow[i-1] * 2)

    ans = 1
    for i in range(1, m_min+1):
        ans += fac[n]/(fac[i] * fac[n - 2*i] * twoPow[i])

    return int(ans)

def func_better(n):
    arr = [1, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + (i-1)*arr[i-2])

    return arr[n]

if __name__ == '__main__':
    n = int(input())
    print(func_better(n))