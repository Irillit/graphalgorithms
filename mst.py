class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

class Graph:
    def __init__(self):
        self.MAX = 20
        self.stack = []
        self.vertexes = []
        self.adj = [[0 for x in range(self.MAX)] for y in range(self.MAX)]

    def add_vertex(self, label):
        self.vertexes.append(Vertex(label))

    def add_edge(self, v1, v2):
        self.adj[v1][v2] = 1
        self.adj[v2][v1] = 1

    def get_adj(self, v):
        for j in range(len(self.vertexes)):
            if self.adj[j][v] == 1 and not self.vertexes[j].visited:
                return j
        return -1

    def mst(self):
        self.vertexes[0].visited = True
        self.stack.append(0)

        while len(self.stack) > 0:
            current = self.stack[-1]
            v = self.get_adj(current)
            if v != -1:
                self.vertexes[v].visited = True
                self.stack.append(v)

                current_label = self.vertexes[current].label
                next_label = self.vertexes[v].label
                print("{} -> {}".format(current_label, next_label))
            else:
                self.stack.pop()

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D') 
    graph.add_vertex('E')

    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 4)

    graph.mst()
