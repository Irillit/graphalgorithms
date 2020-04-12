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

    def dfs(self):
        self.vertexes[0].visited = True
        print(self.vertexes[0].label)
        self.stack.append(0)

        while len(self.stack) > 0:
            v = self.get_adj(self.stack[-1])
            if v != -1:
                self.vertexes[v].visited = True
                print(self.vertexes[v].label)
                self.stack.append(v)
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
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.dfs()
