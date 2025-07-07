# Matrix Operations in Python

A collection of efficient algorithms for common matrix operations and manipulations implemented in Python.

## 📋 Table of Contents

- [Overview](#overview)
- [Mathematical Background](#mathematical-background)
- [Features](#features)
- [Files Description](#files-description)
- [Usage Examples](#usage-examples)
- [Algorithms](#algorithms)
- [Time Complexity](#time-complexity)
- [Requirements](#requirements)
- [Contributing](#contributing)

## 🔍 Overview

This repository contains implementations of fundamental matrix algorithms commonly used in competitive programming, data structures, and algorithmic problem-solving. Each implementation focuses on clarity, efficiency, and practical usage.

## 🧮 Mathematical Background

### Matrix Fundamentals

A **matrix** is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. In computer science, matrices are typically represented as 2D arrays where each element can be accessed using row and column indices.

For an m×n matrix A:
```
A = [a₁₁  a₁₂  ...  a₁ₙ]
    [a₂₁  a₂₂  ...  a₂ₙ]
    [ ⋮    ⋮   ⋱    ⋮ ]
    [aₘ₁  aₘ₂  ...  aₘₙ]
```

### Key Matrix Properties

#### **Diagonals**
- **Primary (Main) Diagonal**: Elements where row index equals column index (i = j)
- **Secondary (Anti) Diagonal**: Elements where row index + column index = n-1
- **Diagonal Sum**: Sum of elements on both diagonals, crucial in linear algebra applications

#### **Sorted Matrices**
- **Row-wise Sorted**: Each row is sorted in ascending order
- **Column-wise Sorted**: Each column is sorted in ascending order
- **Monotonic Property**: Enables efficient searching algorithms like staircase search

#### **Spiral Traversal**
- **Clockwise Spiral**: Traversal pattern moving right→down→left→up
- **Layer-based Approach**: Processing matrix in concentric rectangular layers
- **Applications**: Image processing, matrix printing, data visualization

### Theoretical Applications

#### **Linear Algebra**
- **Diagonal matrices**: Matrices where non-diagonal elements are zero
- **Trace of matrix**: Sum of diagonal elements (implemented in diagonal_sum.py)
- **Matrix decomposition**: Diagonal sums are fundamental in eigenvalue computations

#### **Graph Theory**
- **Adjacency matrices**: Represent graph connections using 2D arrays
- **Path finding**: Sorted matrix search algorithms useful in weighted graph problems
- **Spiral traversal**: Used in maze solving and pathfinding algorithms

#### **Computational Geometry**
- **Coordinate transformations**: Matrices represent geometric transformations
- **Spatial data structures**: 2D arrays for representing grids and spatial relationships
- **Pattern recognition**: Spiral patterns in image processing and computer vision

#### **Algorithm Design Patterns**
- **Divide and Conquer**: Matrix operations often use recursive subdivision
- **Dynamic Programming**: 2D DP tables for optimization problems
- **Greedy Algorithms**: Staircase search demonstrates greedy choice property

## ✨ Features

- **Diagonal Sum Calculation**: Efficiently calculate the sum of primary and secondary diagonals
- **Matrix Creation and Manipulation**: Create, populate, and modify 2D arrays
- **Sorted Matrix Search**: Fast search algorithm for sorted matrices using staircase approach
- **Spiral Matrix Generation**: Generate matrices filled in spiral order
- Clean, readable code with comprehensive examples

## 📁 Files Description

### `diagnol_sum.py`
Calculates the sum of both primary and secondary diagonals of a square matrix.
- Handles the center element correctly for odd-sized matrices
- Time complexity: O(n)
- Space complexity: O(1)

### `implementation.py`
Demonstrates basic 2D array operations including:
- Creating matrices with specified dimensions
- Populating arrays with calculated values
- Accessing and modifying specific elements
- Displaying matrices in formatted output

### `search_in_sorted_matrix.py`
Implements the staircase search algorithm for finding elements in row-wise and column-wise sorted matrices.
- Starts from top-right corner for optimal searching
- Time complexity: O(m + n)
- Space complexity: O(1)

### `spiral_matrix.py`
Generates an n×n matrix filled with numbers in spiral order (clockwise).
- Uses boundary-based approach for efficient traversal
- Time complexity: O(n²)
- Space complexity: O(n²)

## 🚀 Usage Examples

### Diagonal Sum
```python
from diagnol_sum import diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = diagonal_sum(matrix)
print(f"Diagonal Sum: {result}")  # Output: 25
```

### Matrix Search
```python
from search_in_sorted_matrix import staircase_search

matrix = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10, 13, 14, 17]
]

found = staircase_search(matrix, 9)
print(f"Element found: {found}")  # Output: True
```

### Spiral Matrix Generation
```python
from spiral_matrix import generate_spiral_matrix

spiral = generate_spiral_matrix(4)
# Output:
# [1,  2,  3,  4]
# [12, 13, 14, 5]
# [11, 16, 15, 6]
# [10, 9,  8,  7]
```

## 🧮 Algorithms

### Diagonal Sum Algorithm

**Mathematical Foundation:**
For a square matrix A of size n×n, the diagonal sum is calculated as:
```
Diagonal Sum = Σ(i=0 to n-1) A[i][i] + Σ(i=0 to n-1) A[i][n-1-i]
```

**Special Case Handling:**
- For odd-sized matrices, the center element A[n/2][n/2] is counted twice
- Correction: Subtract the center element once to avoid double counting

**Implementation Details:**
- **Approach**: Single pass through matrix diagonals
- **Key insight**: Handle center element in odd-sized matrices to avoid double counting
- **Use cases**: Matrix trace calculation, linear algebra operations

### Staircase Search Algorithm

**Mathematical Foundation:**
Based on the monotonic property of sorted matrices where:
- Each row is sorted: A[i][j] ≤ A[i][j+1]
- Each column is sorted: A[i][j] ≤ A[i+1][j]

**Algorithm Logic:**
Starting from top-right corner (0, n-1):
```
If current > target: Move left (eliminate column)
If current < target: Move down (eliminate row)
If current = target: Found
```

**Implementation Details:**
- **Approach**: Start from top-right corner and eliminate rows/columns based on comparison
- **Key insight**: Leverages sorted property to achieve linear time complexity
- **Use cases**: Database queries, sorted data search, competitive programming

### Spiral Matrix Algorithm

**Mathematical Foundation:**
Spiral traversal follows a pattern of decreasing rectangular boundaries:
```
Layer 0: Outer boundary (full matrix)
Layer 1: Inner boundary (excluding outermost ring)
...
Layer k: Innermost boundary
```

**Traversal Pattern:**
For each layer, traverse in order:
1. **Right**: top row from left to right
2. **Down**: right column from top to bottom
3. **Left**: bottom row from right to left (if rows remain)
4. **Up**: left column from bottom to top (if columns remain)

**Implementation Details:**
- **Approach**: Layer-by-layer traversal using boundary variables
- **Key insight**: Traverse in four directions (right→down→left→up) while shrinking boundaries
- **Use cases**: Matrix printing, image processing, data visualization

### Complexity Analysis Theory

**Time Complexity Fundamentals:**
- **Linear O(n)**: Diagonal sum processes each diagonal element once
- **Linear O(m+n)**: Staircase search eliminates one row or column per iteration
- **Quadratic O(n²)**: Spiral generation must visit every matrix element

**Space Complexity Considerations:**
- **In-place algorithms**: Diagonal sum and staircase search use O(1) extra space
- **Output-dependent**: Spiral generation requires O(n²) space for result matrix

## ⏱️ Time Complexity

| Algorithm | Time Complexity | Space Complexity | Best Use Case |
|-----------|----------------|------------------|---------------|
| Diagonal Sum | O(n) | O(1) | Square matrices |
| Staircase Search | O(m + n) | O(1) | Sorted matrices |
| Spiral Generation | O(n²) | O(n²) | Pattern generation |

## 🔧 Requirements

- Python 3.6+
- No external dependencies required

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include test cases for new algorithms
- Maintain existing code formatting

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Related Topics

### Mathematical Concepts
- **Linear Algebra**: Matrix operations, eigenvalues, matrix decomposition
- **Discrete Mathematics**: Combinatorics, graph theory applications
- **Number Theory**: Matrix properties and mathematical patterns

### Computer Science Applications
- **Dynamic Programming**: 2D DP tables and optimization problems
- **Graph Algorithms**: Adjacency matrices and shortest path algorithms
- **Computational Geometry**: Coordinate transformations and spatial data structures
- **Image Processing**: Pixel manipulation and pattern recognition
- **Database Systems**: Multi-dimensional indexing and query optimization

### Algorithm Design Paradigms
- **Divide and Conquer**: Matrix multiplication and recursive algorithms
- **Greedy Algorithms**: Optimal substructure in matrix problems
- **Two-Pointer Technique**: Efficient matrix traversal patterns
- **Sliding Window**: Submatrix problems and optimization

### Advanced Topics
- **Sparse Matrices**: Memory-efficient storage for matrices with many zeros
- **Matrix Decomposition**: LU, QR, SVD decompositions
- **Parallel Computing**: Matrix operations on multi-core systems
- **GPU Computing**: Matrix operations on graphics processing units

---

⭐ **Star this repository if you find it helpful!**
