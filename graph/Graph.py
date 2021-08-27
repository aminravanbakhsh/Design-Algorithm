class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * vertices

    def addEdge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def getEdge(self, i):
        edges = []
        temp = self.graph[i]
        while(temp):
            edges.append(temp.data)
            temp = temp.next

        return edges

    def printGraph(self):

        for i in range(self.V):
            temp = self.graph[i]

            print(i, ": ", end="")

            while(temp):
                print("-> {}".format(temp.data), end=", ")
                temp = temp.next

            print()

class DirectedGraph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * vertices

    def addEdge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    def getEdge(self, i):
        edges = []
        temp = self.graph[i]
        while(temp):
            edges.append(temp.data)
            temp = temp.next

        return edges

    def getT(self):
        graphT = DirectedGraph(self.V)

        for i in range(self.V):
            edges = self.getEdge(i)
            for edge in edges:
                graphT.addEdge(edge, i)

        return graphT

    def printGraph(self):

        for i in range(self.V):
            temp = self.graph[i]

            print(i, ": ", end="")

            while(temp):
                print("-> {}".format(temp.data), end=", ")
                temp = temp.next

            print()

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if not self.first:
            self.first = node
            self.last = node

        else:
            self.last.next = node
            self.last = node

        self.size += 1


    def pop(self):
        if not self.first:
            return None
        elif self.first == self.last:
            first = self.first.data
            self.first = None
            self.last = None
            self.size -= 1
            return first
        else:
            first = self.first.data
            self.first = self.first.next
            self.size -= 1
            return first

class Stack:

    def __init__(self):
        self.last = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        node.next = self.last
        self.last = node
        self.size += 1

    def pop(self):
        node = self.last
        if node != None:
            self.last = node.next
            self.size -= 1
            return node.data

        return None

    def popAll(self):
        vals = []
        x = self.pop()
        while(x != None):
            vals.append(x)
            x = self.pop()

        return vals

if __name__ == '__main__':

    # graph = DirectedGraph(4)
    # graph.addEdge(0,1)
    # graph.addEdge(0,2)
    # graph.addEdge(0,3)
    # graph.addEdge(1,2)
    # graph.addEdge(2,3)
    #
    # graph.printGraph()
    # graph.getT().printGraph()

    stack = Stack()
    stack.add(1)
    stack.add(2)
    stack.add(3)
    stack.add(4)
    x = stack.popAll()
    print(x)