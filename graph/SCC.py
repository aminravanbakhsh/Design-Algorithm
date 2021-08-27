from Graph import DirectedGraph
from Graph import Stack

def DFS(graph, idx, check, stack, timeStack):
    stack.add(idx)
    edges = graph.getEdge(idx)
    check[idx] = True
    for val in edges:
        if not check[val]:
            DFS(graph, val, check, stack, timeStack)

    x = stack.pop()
    timeStack.add(x)


def kosaraju(graph):
    check = [False] * graph.V
    stack = Stack()
    timeStack = Stack()
    for i in range(graph.V):
        if not check[i]:
            DFS(graph, i, check, stack, timeStack)



    graphT = graph.getT()
    check = [False] * graph.V

    scc = []
    while(timeStack.size):
        x = timeStack.pop()
        if not check[x]:
            stack = Stack()
            saveStack = Stack()
            DFS(graph, x, check, stack, saveStack)
            scc.append(saveStack.popAll())
    return scc

if __name__ == '__main__':

    print("enter count of vertices and edges then enter source and destination of edges:")
    V, E = map(int, input().split())
    graph = DirectedGraph(V)
    for i in range(E):
        s, d = map(int, input().split())
        graph.addEdge(s, d)

    scc = kosaraju(graph)
    print(scc)

"""
4 5
0 1
0 2
1 3
2 3
3 1

"""