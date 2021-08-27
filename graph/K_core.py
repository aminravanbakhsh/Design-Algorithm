from Graph import Graph

def DFS(graph, idx, k, cores):
    edges = graph.getEdge(idx)

    if cores[idx] < k:
        cores[idx] = -1
        for edge in edges:
            if cores[edge] != -1:
                cores[edge] -= 1
                if cores[edge] < k:
                    DFS(graph, edge, k, cores)

def kCore(graph, k):
    cores = [-1] * graph.V
    less = []
    for i in range(graph.V):
        cores[i] = len(graph.getEdge(i))
        if cores[i] < k:
            less.append(i)

    for i in less:
        DFS(graph, i, k , cores)

    kcores = []
    for i in range(graph.V):
        if cores[i] != -1:
            kcores.append(i)

    return kcores

if __name__ == '__main__':
    graph = Graph(9)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 5)
    graph.addEdge(2, 5)
    graph.addEdge(5, 8)
    graph.addEdge(8, 6)
    graph.addEdge(2, 6)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(4, 3)
    graph.addEdge(4, 6)
    graph.addEdge(4, 7)
    graph.addEdge(3, 6)
    graph.addEdge(3, 7)
    graph.addEdge(6, 7)
    print(kCore(graph, 3))
