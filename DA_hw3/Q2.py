def func(n, m, edges):
    for edge in edges:
        edge[0] -= 1
        edge[1] -= 1

    edges.sort(key=lambda x: x[2])
    # [print(x) for x in edges]

    check = [False for i in range(m)]
    nodes = [-1 for i in range(n)]
    comps = [[] for i in range(n)]
    k, p, q = 0, 0, 0
    while p < m:
        q = p + 1
        while q < m:
            if edges[q][2] == edges[p][2]:
                q += 1
            else:
                break

        for i in range(p, q):
            test1 = edges[i][0]
            test2 = edges[i][1]
            if (nodes[edges[i][0]] != nodes[edges[i][1]] or nodes[edges[i][0]] == -1):
                check[edges[i][3]] = True

        for i in range(p, q):
            v1, v2 = edges[i][0], edges[i][1]
            if nodes[v1] == -1 and nodes[v2] == -1:
                comps[k] = [v1, v2]
                nodes[v1], nodes[v2] = k, k
                k += 1

            elif nodes[v1] == -1:
                comps[nodes[v2]].append(v1)
                nodes[v1] = nodes[v2]

            elif nodes[v2] == -1:
                comps[nodes[v1]].append(v2)
                nodes[v2] = nodes[v1]

            elif nodes[v1] != nodes[v2]:
                k1, k2 = nodes[v1], nodes[v2]
                comp_small, comp_big = 0, 0
                k_small, k_big = -1, -1

                if len(comps[k1]) < len(comps[k2]):
                    comp_small, comp_big = comps[k1], comps[k2]
                    k_small, k_big = k1, k2
                else:
                    comp_small, comp_big = comps[k2], comps[k1]
                    k_small, k_big = k2, k1

                c_small = len(comp_small)

                for j in range(c_small):
                    nodes[comp_small[j]] = k_big
                    comp_big.append(comp_small[j])

                comp_small = []

        p = q

    return check

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        x = list(map(int, input().split()))
        x.append(i)
        edges.append(x)

    check = func(n,m,edges)
    for c in check:
        if c:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()

'''
3 3
1 2 30
1 3 40
2 3 10

3 3
1 2 10
1 3 10
3 2 10

5 6
1 2 10
1 3 10
3 2 10
1 5 5
3 4 6
4 5 7



'''