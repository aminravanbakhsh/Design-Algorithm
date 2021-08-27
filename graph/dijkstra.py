import copy as cp

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in  range(V)]

    def addEdge(self,src, dst, val):
        self.graph[src].append([dst, val])

    def getEdges(self, idx):
        return self.graph[idx]

def findIdx2(array, val):
    arr = [-1]
    arr.extend(array)
    k = len(arr)
    r = k
    l = 0
    i = k // 2

    while(not(r == i or l == i)):
        if arr[i] == val:
            return i - 1
        elif val > arr[i]:
            l = i
            i = (i+1+r)//2
        else:
            r = i
            i = (i-1+l)//2

    return i-1

def findIdx(array, val):
    arr = [-1]
    arr.extend(array)
    k = len(arr)
    r = k
    l = 0
    i = int(k/2)

    while(not(arr[i] == val or r == i or l == i)):
        if arr[i] > val:
            r = i
            i = int((i + l)/2)
        else:
            l = i
            i = int((r + i)/2)

    if k <= 2:
        return i

    if arr[i] < val:
        return i
    return i - 1


def dijkstra(graph, src, dst):
    queue = []
    srcs = []
    dsts = []
    visited = [False] * graph.V
    visited[src] = True

    edges = graph.getEdges(src)
    for edge in edges:
        idx = findIdx(queue, edge[1])
        queue.insert(idx, edge[1])
        srcs.insert(idx, src)
        dsts.insert(idx, edge)

    i = 0
    while(not dsts[i][0] == dst):
        if not visited[dsts[i][0]]:
            visited[dsts[i][0]] = True
            edges = graph.getEdges(dsts[i][0])
            for edge in edges:
                if not visited[edge[0]]:
                    idx = findIdx(queue, queue[i] + edge[1])
                    queue.insert(idx, queue[i] + edge[1])
                    srcs.insert(idx, srcs[i])
                    dsts.insert(idx, edge)

        i += 1

    return queue[i]

if __name__ == '__main__':
    # graph = Graph(5)
    # graph.addEdge(0,1,8)
    # graph.addEdge(1,3,7)
    # graph.addEdge(3,4,4)
    # graph.addEdge(0,2,12)
    # graph.addEdge(2,4,8)
    # graph.addEdge(2, 3, 1)
    # print(dijkstra(graph, 0, 4))

    arr = [9]
    k = 8
    print(findIdx(arr,k))
    print(findIdx2(arr,k))