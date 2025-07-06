class Graph:
    def __init__(self):
        self.edges = []
    
    def add_edge(self,u,v):
        self.edges.append((u,v))
    
    def display(self):
        for edge in self.edges:
            print(edge)

# Example Usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

graph.display()