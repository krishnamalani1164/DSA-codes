# Segment Tree Implementation

A comprehensive implementation of Segment Trees in Python for efficient range queries and updates.

## Table of Contents
- [Overview](#overview)
- [Theory](#theory)
- [Implementation Logic](#implementation-logic)
- [Files](#files)
- [Usage Examples](#usage-examples)
- [Time Complexity](#time-complexity)
- [Applications](#applications)

## Overview

Segment Trees are binary tree data structures that allow efficient range queries and point updates on arrays. This repository provides three implementations:
- **Range Sum Queries** (`segment_tree.py`)
- **Range Maximum Queries** (`range_max_st.py`)
- **Range Minimum Queries** (`range_min_st.py`)

## Theory

### What is a Segment Tree?

A Segment Tree is a binary tree where:
- Each leaf node represents a single array element
- Each internal node represents a segment (range) of the array
- The root represents the entire array
- Each node stores the result of an operation (sum, min, max, etc.) over its segment

### Why Use Segment Trees?

Traditional approaches for range queries have limitations:
- **Naive approach**: O(n) per query, O(1) per update
- **Prefix arrays**: O(1) per query, O(n) per update
- **Segment Trees**: O(log n) per query, O(log n) per update

This balanced performance makes segment trees ideal for scenarios with frequent queries and updates.

### Tree Structure

For an array of size `n`, the segment tree:
- Has at most `4n` nodes (allocated for simplicity)
- Uses 0-based indexing where node `i` has children at `2i+1` and `2i+2`
- Stores the operation result (sum/min/max) for each segment

```
Array: [1, 3, 5, 7, 9, 11]
Tree representation for sum:
                36
              /    \
           9          27
         /   \      /    \
       4      5   16     11
      / \    /   / \    /
     1   3  5   7   9  11
```

## Implementation Logic

### 1. Building the Tree

The `build()` function constructs the tree bottom-up:

```python
def build(self, arr, node, start, end):
    if start == end:
        self.tree[node] = arr[start]  # Leaf node
    else:
        mid = (start + end) // 2
        self.build(arr, 2 * node + 1, start, mid)      # Left child
        self.build(arr, 2 * node + 2, mid + 1, end)    # Right child
        self.tree[node] = operation(left_child, right_child)  # Merge results
```

**Logic**: 
- Base case: If segment has one element, store it directly
- Recursive case: Build left and right subtrees, then combine their results
- Time complexity: O(n)

### 2. Range Queries

The `query()` function handles three cases:

```python
def query(self, node, start, end, l, r):
    if r < start or end < l:
        return identity_value  # No overlap
    if l <= start and end <= r:
        return self.tree[node]  # Total overlap
    # Partial overlap - recurse on both children
    mid = (start + end) // 2
    left = self.query(2 * node + 1, start, mid, l, r)
    right = self.query(2 * node + 2, mid + 1, end, l, r)
    return operation(left, right)
```

**Logic**:
- **No overlap**: Query range doesn't intersect with current segment
- **Total overlap**: Current segment is completely within query range
- **Partial overlap**: Query range partially intersects - check both children
- Time complexity: O(log n)

### 3. Point Updates

The `update()` function modifies a single element:

```python
def update(self, node, start, end, idx, value):
    if start == end:
        self.tree[node] = value  # Update leaf
    else:
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, value)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, value)
        self.tree[node] = operation(left_child, right_child)  # Update internal node
```

**Logic**:
- Navigate to the leaf node containing the target index
- Update the leaf value
- Propagate changes up to the root by recalculating internal nodes
- Time complexity: O(log n)

## Files

### `segment_tree.py`
- **Operation**: Range Sum Query
- **Identity**: 0 (for no overlap cases)
- **Use case**: Finding sum of elements in any range

### `range_max_st.py`
- **Operation**: Range Maximum Query
- **Identity**: -∞ (for no overlap cases)
- **Use case**: Finding maximum element in any range

### `range_min_st.py`
- **Operation**: Range Minimum Query
- **Identity**: +∞ (for no overlap cases)
- **Use case**: Finding minimum element in any range

## Usage Examples

### Range Sum Queries
```python
from segment_tree import SegmentTree

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

# Query sum from index 1 to 3
result = st.query(0, 0, st.n - 1, 1, 3)  # Returns 15 (3+5+7)

# Update index 1 to value 10
st.update(0, 0, st.n - 1, 1, 10)

# Query again
result = st.query(0, 0, st.n - 1, 1, 3)  # Returns 22 (10+5+7)
```

### Range Maximum Queries
```python
from range_max_st import SegmentTreeMax

arr = [2, 1, 5, 3, 9, 7]
st = SegmentTreeMax(arr)

# Find maximum from index 1 to 4
max_val = st.query(0, 0, st.n - 1, 1, 4)  # Returns 9

# Update index 2 to 10
st.update(0, 0, st.n - 1, 2, 10)

# Find maximum again
max_val = st.query(0, 0, st.n - 1, 1, 4)  # Returns 10
```

### Range Minimum Queries
```python
from range_min_st import SegmentTreeMin

arr = [4, 2, 1, 5, 3]
st = SegmentTreeMin(arr)

# Find minimum from index 1 to 3
min_val = st.query(0, 0, st.n - 1, 1, 3)  # Returns 1

# Update index 2 to 6
st.update(0, 0, st.n - 1, 2, 6)

# Find minimum again
min_val = st.query(0, 0, st.n - 1, 1, 3)  # Returns 2
```

## Time Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build     | O(n)           | O(n)             |
| Query     | O(log n)       | O(1)             |
| Update    | O(log n)       | O(1)             |

## Applications

### Practical Use Cases
- **Database Range Queries**: Efficiently query aggregated data over ranges
- **Stock Market Analysis**: Find maximum/minimum prices in time windows
- **Gaming**: Range damage calculations, area-of-effect queries
- **Computational Geometry**: Range searching in 1D space
- **Statistics**: Dynamic range statistics with updates

### Competitive Programming
- **Range Sum/Min/Max Queries**: Direct application
- **Lazy Propagation**: Can be extended for range updates
- **2D Segment Trees**: For 2D range queries
- **Persistent Segment Trees**: For historical queries

## Advanced Extensions

This implementation can be extended to support:
- **Range Updates**: Modify multiple elements efficiently
- **Lazy Propagation**: Defer updates for better performance
- **2D Segment Trees**: Handle 2D range queries
- **Generic Operations**: Support any associative operation
- **Persistent Trees**: Maintain multiple versions

## Contributing

Feel free to contribute by:
- Adding new operation types
- Implementing lazy propagation
- Adding more comprehensive examples
- Improving documentation

## License

This project is open source and available under the MIT License.
