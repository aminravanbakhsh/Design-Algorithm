if __name__ == '__main__':
    arr = [13]

    for i in range(1, 10):
        arr.append(arr[i-1]*i)

    for val in arr:
        print(val)