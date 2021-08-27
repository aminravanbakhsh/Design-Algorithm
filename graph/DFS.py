from Graph import DirectedGraph
from Graph import Stack
from Graph import Queue

def DFS(graph, src):
    check = [False] * graph.V
    stack = Stack()
    __DFS_body(graph, src, check, stack)

def __DFS_body(graph, idx, check, stack):
    stack.add(idx)
    edges = graph.getEdge(idx)
    check[idx] = True
    for val in edges:
        if not check[val]:
            __DFS_body(graph, val, check, stack)

    x = stack.pop()
    print(x)

if __name__ == '__main__':
    graph = DirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 3)
    graph.addEdge(3, 4)
    DFS(graph, 2)