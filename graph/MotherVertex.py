from Graph import DirectedGraph
from Graph import Stack

def goToMotherVertex(graph, idx, check, stack):
    stack.add(idx)
    edges = graph.getEdge(idx)
    check[idx] = True
    for val in edges:
        if not check[val]:
            goToMotherVertex(graph, val, check, stack)

def DFS(graph, idx, check, stack):
    stack.add(idx)
    edges = graph.getEdge(idx)
    check[idx] = True
    for val in edges:
        if not check[val]:
            DFS(graph, val, check, stack)

    x = stack.pop()

def getMotherVertex(graph):
    v = graph.V
    graphT = graph.getT()
    src = 0
    check = [False] * v
    stack = Stack()
    goToMotherVertex(graphT, 0, check, stack)
    motheridx = stack.pop()
    check = [False] * v
    stack = Stack()
    DFS(graph, motheridx, check, stack)
    if all(check):
        return motheridx
    else:
        return None

if __name__ == '__main__':
    graph = DirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 3)
    graph.addEdge(3, 4)
    print(getMotherVertex(graph))