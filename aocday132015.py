#AOC Day 13 2015
#Read text file input
with open('aocday132015.txt') as f:
    lines = f.readlines()

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph
 
 
# Class to represent a graph
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
 
            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
 
    # The main function to construct MST
    # using Kruskal's algorithm
    def KruskalMST(self):
 
        # This will store the resultant MST
        result = []
 
        # An index variable, used for sorted edges
        i = 0
 
        # An index variable, used for result[]
        e = 0
 
        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:
 
            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
 
def interpretInput() :
    vertices = []
    connectivity = {}
    for line in lines :
        splitted_by_spaces = line.split(" ")
        first_node, sign, value, second_node = splitted_by_spaces[0], splitted_by_spaces[2], splitted_by_spaces[3], splitted_by_spaces[-1][:-2]
        if not first_node in vertices :
            vertices.append(first_node)
        if not second_node in vertices :
            vertices.append(second_node)
        value = int(value)
        if sign == "lose" :
            value = -value
        firstNodeIndex, secondNodeIndex = vertices.index(first_node), vertices.index(second_node)
        if (secondNodeIndex, firstNodeIndex) in connectivity :
            connectivity[(secondNodeIndex, firstNodeIndex)] -= value
        else :
            connectivity[(firstNodeIndex, secondNodeIndex)] = -value
    print(vertices, connectivity)
    return connectivity, len(vertices)


# Driver code
if __name__ == '__main__':
    connect, V = interpretInput()
    g = Graph(V)
    for c in connect :
        g.addEdge(c[0], c[1], connect[c])
 
    # Function call
    g.KruskalMST()

