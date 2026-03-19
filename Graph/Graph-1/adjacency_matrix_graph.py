class Graph:
    def __init__(self,size):
        self.size = size
        self.matrix = [[0]*size for _ in range(size)]

    def add_edge(self,u,v):
        self.matrix[u][v] = 1

        self.matrix[v][u] = 1
    
    def display(self):
        for row in self.matrix:
            print(row)

# Example Usage
graph = Graph(5)  # 5 nodes (0 to 4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.display()

