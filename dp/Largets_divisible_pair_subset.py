import copy

def func(arr):
    ws = sorted(arr)
    n = len(ws)
    pair_size = [0 for i in range(n)]
    pair_size[0] = 1
    max_pair = [[] for i in range(n)]
    max_pair[0] = [ws[0]]

    for i in range(1, n):
        temp_pair_size = copy.deepcopy(pair_size)
        temp_max_pair = copy.deepcopy(max_pair)

        for j in range(i):
            if ws[i] % ws[j] == 0:
                if pair_size[j] + 1 > temp_pair_size[i]:
                    temp_max_pair[i] = copy.deepcopy(max_pair[j])
                    temp_max_pair[i].append(ws[i])
                    temp_pair_size[i] = 1 + pair_size[j]

        if temp_pair_size[i] == 0:
            temp_max_pair[i] = [ws[i]]
            temp_pair_size[i] = 1

        max_pair = copy.deepcopy(temp_max_pair)
        pair_size = copy.deepcopy(temp_pair_size)

    max_size = 0
    max_idx = -1
    for i in range(n):
        if pair_size[i] > max_size:
            max_size = pair_size[i]
            max_idx = i

    return max_pair[max_idx]

if __name__ == '__main__':
    ws = list(map(int, input().split()))
    print(func(ws))