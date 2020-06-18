class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

class Graph:
    def __init__(self):
        self.MAX = 20
        self.vertexes = []
        self.adj = [[0 for x in range(self.MAX)] for y in range(self.MAX)]
        self.sorted = [0] * self.MAX
        self.verts = 0

    def add_vertex(self, label):
        self.vertexes.append(Vertex(label))

    def add_edge(self, start, end):
        self.adj[start][end] = 1

    def topo(self):
        self.verts = len(self.vertexes)
        orig_verts = self.verts
        while self.verts > 0:
            cur_vert = self.no_successors()
            if cur_vert == -1:
                print("ERROR: Graph has cycles")
                return
            self.sorted[self.verts - 1] = self.vertexes[cur_vert].label
            self.delete_vertex(cur_vert)

        print("Topologically sorted order: ")
        for i in range(orig_verts):
            print(self.sorted[i], end=' ')

    def no_successors(self):
        for row in range(self.verts):
            is_edge = False
            for col in range(self.verts):
                if self.adj[row][col] > 0:
                    is_edge = True
                    break
            if not is_edge:
                return row
        return -1

    def delete_vertex(self, del_vert):
        if del_vert != self.verts - 1:
            for j in range(del_vert, self.verts - 1):
                self.vertexes[j] = self.vertexes[j+1]

            for row in range(del_vert, self.verts - 1):
                self.move_row_up(row, self.verts)

            for col in range(del_vert, self.verts - 1):
                self.move_col_left(col, self.verts - 1)

        self.verts -= 1

    def move_row_up(self, row, length):
        for col in range(length):
            self.adj[row][col] = self.adj[row + 1][col]

    def move_col_left(self, col, length):
        for row in range(length):
            self.adj[row][col] = self.adj[row][col + 1]

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_vertex('H')
    graph.add_edge(0, 3)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    graph.topo()
