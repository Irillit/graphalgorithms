class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = []
        for i in range(V):
            self.adj.append([])

    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)
        self.E += 1

    def get_adj(self, v):
        return self.adj[v]


class DepthFirstSearch:

    def __init__(self):
        self.MAX_VER = 20
        self.marked = [False] * self.MAX_VER
        self.has_cycle = False
        self.count = 0
        
    def dfs(self, g: Graph, v: int, u: int):
        self.marked[v] = True
        self.count += 1
        for w in g.get_adj(v):
            if not self.marked[w]:
                print(w)
                self.dfs(g, w, v)
            elif w != u:
                self.has_cycle = True

if __name__ == "__main__":
    gr = Graph(5)
    gr.add_edge(0, 1)
    gr.add_edge(1, 3)
    gr.add_edge(1, 2)
    gr.add_edge(3, 4)
    gr.add_edge(4, 2)

    dfs = DepthFirstSearch()
    dfs.dfs(gr, 0, 0)
    print("Count: " + str(dfs.count))
    print("Cycle: " + str(dfs.has_cycle))
