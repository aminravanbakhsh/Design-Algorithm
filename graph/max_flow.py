import copy as cp

class Graph:

    def __init__(self, n, graph):
        self.n = n
        self.org_graph = graph
        self.graph = cp.deepcopy(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.n
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for i in range(n):
                if (not visited[i]) and self.graph[u][i] > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u

        return True if visited[t] else False


    def maxFlow(self, s, t):
        parent = [-1] * self.n
        maxflow = 0
        while self.BFS(s, t, parent):
            min_path = float('inf')
            p = t
            while (p != s):
                z = parent[p]
                if self.graph[z][p] < min_path:
                    min_path = self.graph[z][p]

                p = z

            maxflow += min_path

            p = t
            while(p != s):
                z = parent[p]
                self.graph[z][p] -= min_path
                self.graph[p][z] += min_path
                p = z

        return maxflow

if __name__ == '__main__':
    n, m  = map(int, input().split())
    s, t = map(int, input().split())
    g = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        x, y, w = map(int, input().split())
        g[x][y] = w

    graph = Graph(n, g)
    print(graph.maxFlow(s,t))

'''
4 5
0 3
0 1 3
0 2 5
2 1 2
1 3 6
2 3 2


'''