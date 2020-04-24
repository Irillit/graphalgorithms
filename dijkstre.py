class DistPar:
    def __init__(self, pv, d):
        self.distance = d
        self.parent = pv

class Vertex:
    def __init__(self, label):
        self.label = label
        self.isInTree = False

class Graph:
    def __init__(self):
        self.MAX = 20
        self.INFINITY = 100000000
        self.vertexes = []
        self.n_verts = 0
        self.n_tree = 0
        self.sPath = []
        self.adj = []
        self.current = 0
        self.start_to_current = 0
        for _ in range(self.MAX):
            self.adj.append([])
        for j in range(self.MAX):
            for _ in range(self.MAX):
                self.adj[j].append(self.INFINITY)
                
    def addVertex(self, label):
        self.n_verts += 1
        if self.n_verts < self.MAX:
            self.vertexes.append(Vertex(label))

    def addEdge(self, start, end, weight):
        self.adj[start][end] = weight

    def getMin(self):
        minDist = self.INFINITY
        indexMin = 0

        for j in range(1, self.n_verts):
            if not self.vertexes[j].isInTree and \
               self.sPath[j].distance < minDist:
                minDist = self.sPath[j].distance
                indexMin = j
        return indexMin

    def adjust_sPath(self):
        column = 1
        while column < self.n_verts:
            if self.vertexes[column].isInTree:
                column += 1
                continue
            currentToFringe = self.adj[self.currentVert][column]
            startToFringe = self.startToCurrent + currentToFringe
            sPathDist = self.sPath[column].distance
            if startToFringe < sPathDist:
                self.sPath[column].parent = self.currentVert
                self.sPath[column].distance = startToFringe
            column += 1

    def displayPaths(self):
        for j in range(self.n_verts):
            print("{}=".format(self.vertexes[j].label), end=' ')
            if self.sPath[j].distance == self.INFINITY:
                print("inf")
            else:
                print(self.sPath[j].distance)
            parent = self.vertexes[self.sPath[j].parent].label
            print("({}) ".format(parent))

    def path(self):
        startTree = 0
        self.vertexes[startTree].isInTree = True
        self.n_tree = 1

        for j in range(self.n_verts):
            tmp = self.adj[startTree][j]
            self.sPath.append(DistPar(startTree, tmp))

        while self.n_tree < self.n_verts:
            indexMin = self.getMin()
            minDist = self.sPath[indexMin].distance

            if minDist == self.INFINITY:
                print("There are unreachable vertices")
                break
            else:
                self.currentVert = indexMin
                self.startToCurrent = self.sPath[indexMin].distance
            self.vertexes[self.currentVert].isInTree = True
            self.n_tree += 1
            self.adjust_sPath()
        
        self.displayPaths()
        
        self.n_tree = 0
        for j in range(self.n_verts):
            self.vertexes[j].isInTree = False
                

if __name__ == "__main__":
    theGraph = Graph()
    theGraph.addVertex('A')
    theGraph.addVertex('B')
    theGraph.addVertex('C')
    theGraph.addVertex('D')
    theGraph.addVertex('E')

    theGraph.addEdge(0, 1, 50)
    theGraph.addEdge(0, 3, 80)
    theGraph.addEdge(1, 2, 60)
    theGraph.addEdge(1, 3, 90)
    theGraph.addEdge(2, 4, 40)
    theGraph.addEdge(3, 2, 20)
    theGraph.addEdge(3, 4, 70)
    theGraph.addEdge(4, 1, 50)

    print("Shortest path")
    theGraph.path()
        
