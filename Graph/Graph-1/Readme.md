# Graph Theory & Algorithms 🔗

A comprehensive collection of graph data structures and algorithms implemented in Python. This repository covers fundamental graph concepts, different representation methods, and essential traversal algorithms.

## 📋 Table of Contents

- [What is a Graph?](#what-is-a-graph)
- [Graph Representations](#graph-representations)
- [Traversal Algorithms](#traversal-algorithms)
- [Files Overview](#files-overview)
- [Getting Started](#getting-started)
- [Problem Solving with Graphs](#problem-solving-with-graphs)
- [Time & Space Complexity](#time--space-complexity)
- [Contributing](#contributing)

## What is a Graph? 🌐

A **graph** is a data structure consisting of:
- **Vertices (Nodes)**: Individual points or entities
- **Edges**: Connections between vertices

Graphs are everywhere in real life: social networks, road maps, computer networks, dependency graphs, and more!

```
Example Graph:
    A ---- B
    |      |
    |      |
    C ---- D
```

### Types of Graphs

- **Undirected Graph**: Edges have no direction (friendship on social media)
- **Directed Graph**: Edges have direction (following on Twitter)
- **Weighted Graph**: Edges have weights/costs (distance between cities)
- **Unweighted Graph**: All edges have equal weight

## Graph Representations 📊

### 1. Edge List
Stores all edges as a list of pairs.

```python
edges = [(1,2), (1,3), (2,4), (3,4)]
```

**Pros:** Simple, memory efficient for sparse graphs
**Cons:** Slow to check if edge exists, slow to find neighbors

### 2. Adjacency List
Each vertex maintains a list of its neighbors.

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
```

**Pros:** Memory efficient, fast neighbor lookup
**Cons:** Slow to check if specific edge exists

### 3. Adjacency Matrix
2D matrix where `matrix[i][j] = 1` if edge exists.

```python
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```

**Pros:** Fast edge existence check, good for dense graphs
**Cons:** Uses O(V²) space, inefficient for sparse graphs

## Traversal Algorithms 🚶‍♂️

### Breadth-First Search (BFS)
Explores graph level by level using a queue.

```
Visual BFS Traversal:
Level 0:    A
Level 1:   / \
          B   C
Level 2:   \ /
            D
```

**Use Cases:**
- Finding shortest path (unweighted)
- Level-order traversal
- Connected components
- Bipartite graph checking

### Depth-First Search (DFS)
Explores as far as possible along each branch using recursion/stack.

```
Visual DFS Traversal:
Path: A → B → D → C
```

**Use Cases:**
- Topological sorting
- Cycle detection
- Strongly connected components
- Maze solving

## Files Overview 📁

| File | Description | Time Complexity |
|------|-------------|----------------|
| `edge_list_graph.py` | Edge list representation | Add: O(1), Display: O(E) |
| `adjacency_list_graph.py` | Adjacency list representation | Add: O(1), Display: O(V+E) |
| `adjacency_matrix_graph.py` | Adjacency matrix representation | Add: O(1), Display: O(V²) |
| `bfs_traversal_graph.py` | Breadth-first search algorithm | O(V + E) |
| `dfs_traversal_graph.py` | Depth-first search algorithm | O(V + E) |

## Getting Started 🚀

### Prerequisites
- Python 3.6+
- No external dependencies required

### Running the Code

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/graph-algorithms.git
cd graph-algorithms
```

2. **Run individual files:**
```bash
python edge_list_graph.py
python adjacency_list_graph.py
python adjacency_matrix_graph.py
python bfs_traversal_graph.py
python dfs_traversal_graph.py
```

3. **Example Usage:**
```python
# Create a graph using adjacency list
from adjacency_list_graph import Graph

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.display()
```

## Problem Solving with Graphs 🧩

### Common Graph Problems

1. **Shortest Path Problems**
   - Use BFS for unweighted graphs
   - Use Dijkstra's algorithm for weighted graphs

2. **Connectivity Problems**
   - Use DFS/BFS to find connected components
   - Check if graph is connected

3. **Cycle Detection**
   - Use DFS with color coding
   - Important for detecting deadlocks

4. **Topological Sorting**
   - Use DFS for ordering dependencies
   - Useful for task scheduling

### Problem-Solving Strategy

1. **Identify the Graph Structure**
   - What are the vertices and edges?
   - Is it directed or undirected?
   - Is it weighted?

2. **Choose the Right Representation**
   - Sparse graph → Adjacency List
   - Dense graph → Adjacency Matrix
   - Simple operations → Edge List

3. **Select the Algorithm**
   - Need shortest path? → BFS (unweighted)
   - Need to explore all paths? → DFS
   - Need specific ordering? → Topological Sort

### Example Problem: Social Network Analysis

```python
# Find mutual friends (intersection of adjacency lists)
def find_mutual_friends(graph, user1, user2):
    friends1 = set(graph[user1])
    friends2 = set(graph[user2])
    return friends1.intersection(friends2)

# Find degrees of separation (shortest path)
def degrees_of_separation(graph, user1, user2):
    # Use BFS to find shortest path
    # Implementation in bfs_traversal_graph.py
    pass
```

## Time & Space Complexity 📊

### Space Complexity Comparison

| Representation | Space Complexity |
|---------------|------------------|
| Edge List | O(E) |
| Adjacency List | O(V + E) |
| Adjacency Matrix | O(V²) |

### Operation Time Complexity

| Operation | Edge List | Adjacency List | Adjacency Matrix |
|-----------|-----------|----------------|------------------|
| Add Edge | O(1) | O(1) | O(1) |
| Check Edge | O(E) | O(degree) | O(1) |
| Get Neighbors | O(E) | O(1) | O(V) |
| Space | O(E) | O(V+E) | O(V²) |

## Key Concepts Summary 🎯

- **Graph**: Collection of vertices connected by edges
- **Traversal**: Systematic way to visit all vertices
- **BFS**: Level-by-level exploration (shortest path)
- **DFS**: Deep exploration (topological sorting, cycle detection)
- **Representation**: Choose based on graph density and required operations

## Contributing 🤝

Contributions are welcome! Here are some ways to contribute:

1. **Add new algorithms**: Dijkstra's, A*, Kruskal's, etc.
2. **Improve visualizations**: Add ASCII art or diagrams
3. **Add more examples**: Real-world problem implementations
4. **Optimize code**: Improve time/space complexity
5. **Add tests**: Unit tests for all implementations

### Steps to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources 📚

- [Graph Theory Visualization](https://visualgo.net/en/graphds)
- [Graph Algorithms Explained](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Interactive Graph Theory](https://d3gt.com/unit.html?graph-theory)

---

**Happy Graph Exploring!** 🎉

If you find this repository helpful, please ⭐ star it and share with others!
