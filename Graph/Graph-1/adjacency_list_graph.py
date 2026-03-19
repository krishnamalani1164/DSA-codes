class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def display(self):
        for node in self.adj_list:
            print(node,":",self.adj_list[node])

# Example Usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

graph.display()