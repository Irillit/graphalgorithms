class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def remove(self):
        return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

class Graph:
    def __init__(self):
        self.MAX_VERTS = 20
        self.vertex_list = []
        self.n_verts = 0
        self.adj_mat = [[0 for x in range(self.MAX_VERTS)] for y in range(self.MAX_VERTS)] 
        self.queue = Queue()

    def add_vertex(self, label):
        self.vertex_list.append(Vertex(label))

    def add_edge(self, start, end):
        self.adj_mat[start][end] = 1
        self.adj_mat[end][start] = 1

    def display_vertex(self, v):
        print(self.vertex_list[v].label)

    def bfs(self):
        self.vertex_list[0].visited = True
        self.display_vertex(0)
        self.queue.insert(0)

        while not self.queue.is_empty():
            v1 = self.queue.remove()
            v2 = self.get_adj_unvisited(v1)
            while v2 != -1:
                self.vertex_list[v2].visited = True
                self.display_vertex(v2)
                self.queue.insert(v2)
                v2 = self.get_adj_unvisited(v1)

        for vert in self.vertex_list:
            vert.visited = False

    def get_adj_unvisited(self, v):
        for j in range(len(self.vertex_list)):
            if self.adj_mat[v][j] == 1 and self.vertex_list[j].visited == False:
                return j
        return -1


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D') 
    graph.add_vertex('E')

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)

    graph.bfs()
