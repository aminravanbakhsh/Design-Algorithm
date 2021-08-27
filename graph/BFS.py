from Graph import DirectedGraph
from Graph import Queue

def BFS(graph, src):
    check = [False] * graph.V
    queue = Queue()
    __BFS_body(graph, src, check, queue)

def __BFS_body(graph, idx, check, queue):

    print(idx)
    check[idx] = True
    edges = graph.getEdge(idx)
    for edge in edges:
        if not check[edge]:
            queue.add(edge)

    idx = queue.pop()
    if idx:
        __BFS_body(graph, idx, check, queue)

if __name__ == '__main__':
    graph = DirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 3)
    graph.addEdge(3, 4)
    BFS(graph, 0)