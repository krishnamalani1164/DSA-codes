def dfs(graph,node,visited):
    if node not in visited:
        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]: #Explore neighbors

            dfs(graph,neighbor,visited)

# Example Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# Perform DFS starting from node 0
visited = set()
dfs(graph, 0, visited)