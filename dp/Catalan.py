def func(n):
    arr = [1,1]

    for i in range(2,n+1):
        x = 0
        for k in range(0,i):
            x += arr[k]*arr[i-1-k]

        arr.append(x)

    return arr[n]

def main():
    n = int(input())
    print(func(n))

if __name__ == '__main__':
    main()