from collections import deque

def bfs(graph,start):
    visited = set()#Track visited nodes

    queue = deque([start])#Initalize the queue

    while queue:
        node = queue.popleft() #Dequeue a node

        if node not in visited:
            print(node, end=" ")#Process the node
            visited.add(node)

            for neighbor in graph[node]: #Loop through neighbors
                if neighbor not in visited:
                    queue.append(neighbor) #Add unvisited node

# Example Graph
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# Perform BFS
bfs(graph, 0)