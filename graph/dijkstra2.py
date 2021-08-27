class Heap:

    def __init__(self, max):
        self.arr = []
        self.l_idx = 0

    def insert(self, val, idx):
        pass

def dijkstra(edges, n, src, tar):

    '''
        edges = [src, tar, w]

    '''

    As = [float('ing') for i in range(n)]
    es = [[] for i in range(n)]
    parents = [-1 for i in range(n)]

    for e in edges:
        es[e[0]].append([e[1], e[2]])

    As[src] = 0
    idx = src
    while idx != tar:


    pass

def main():
    pass

if __name__ == '__main__':
    main()