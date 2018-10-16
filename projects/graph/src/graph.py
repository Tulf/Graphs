"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = set()
        else:
            print("you already have that vertex in this graph")
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v1].add(v2)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
