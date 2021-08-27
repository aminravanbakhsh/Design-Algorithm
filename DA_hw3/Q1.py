import copy as cp

class Graph:

    def __init__(self, n, graph):
        self.n = n
        self.graph = cp.deepcopy(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.n
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for e in self.graph[u]:
                if not visited[e]:
                    queue.append(e)
                    visited[e] = True
                    parent[e] = u

        return True if visited[t] else False

    def maxFlow(self, s, t):
        parent = [-1] * self.n
        maxflow = 0
        while self.BFS(s,t,parent):
            maxflow += 1

            p = t
            while(p != s):
                z = parent[p]
                for i in range(len(self.graph[z])):
                    if self.graph[z][i] == p:
                        h = self.graph[z]
                        self.graph[z].remove(p)
                        break
                self.graph[p].append(z)
                p = z

        return maxflow

if __name__ == '__main__':
    MAX_PATH = 100

    n, xt, yt = map(int, input().split())
    vs = []
    for i in range(n):
        x, y = map(int, input().split())
        vs.append([x,y])
    vs.append([0,0])
    vs.append([xt,yt])

    long = MAX_PATH * MAX_PATH

    G = [[] for i in range(2*n + 2)]

    for i in range(n):
        for j in range(n):
            if i != j and vs[i][0] < vs[j][0]:
                if long >= (vs[i][0] - vs[j][0]) ** 2 + (vs[i][1] - vs[j][1]) ** 2:
                    G[2*i+1].append(2*j)

    for i in range(n):
        if vs[n][0] < vs[i][0]:
            if long > (vs[i][0] - vs[n][0]) ** 2 + (vs[i][1] - vs[n][1]) ** 2:
                G[2*n].append(2*i)

        if vs[i][0] < vs[n+1][0]:
            if long > (vs[i][0] - vs[n+1][0]) ** 2 + (vs[i][1] - vs[n+1][1]) ** 2:
                G[2*i+1].append(2*n+1)

        G[2*i].append(2*i + 1)

    graph = Graph(2*n+2, G)
    print(graph.maxFlow(2*n, 2*n+1))

'''
5 220 0
50 60
50 -60
100 0
160 60
160 -60

2 1000 1000
100 0
200 0

5 240 0
60 60
60 -60
120 0
180 60
180 -60

4 150 100
50 0
50 50
100 50
100 100
'''