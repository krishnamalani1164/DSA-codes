# Binary Search Tree (BST) - Complete Guide

## Table of Contents
- [Introduction](#introduction)
- [BST Properties](#bst-properties)
- [Basic Operations](#basic-operations)
- [Advanced Operations](#advanced-operations)
- [Time Complexity Analysis](#time-complexity-analysis)
- [Common Problems and Solutions](#common-problems-and-solutions)
- [Best Practices](#best-practices)

## Introduction

A **Binary Search Tree (BST)** is a hierarchical data structure that maintains elements in sorted order, enabling efficient search, insertion, and deletion operations. It's a specialized binary tree where each node has at most two children, referred to as left and right subtrees.

## BST Properties

### Fundamental BST Property
For every node in a BST:
- All values in the **left subtree** are **less than** the node's value
- All values in the **right subtree** are **greater than** the node's value
- Both left and right subtrees are also valid BSTs (recursive property)

### Key Characteristics
1. **Ordered Structure**: Inorder traversal of a BST yields elements in sorted order
2. **Unique Values**: Typically, BSTs don't contain duplicate values
3. **Dynamic Size**: Can grow and shrink during runtime
4. **Logarithmic Operations**: Average case time complexity is O(log n) for basic operations

## Basic Operations

### 1. Search Operation
**Purpose**: Find if a specific value exists in the BST

**Algorithm**:
- Start from root
- If target equals current node, return found
- If target is less than current node, search left subtree
- If target is greater than current node, search right subtree
- If we reach null, value doesn't exist

**Time Complexity**: O(log n) average, O(n) worst case

### 2. Insertion Operation
**Purpose**: Add a new value to the BST while maintaining BST property

**Algorithm**:
- Start from root
- Compare new value with current node
- If less, go left; if greater, go right
- Insert at the first null position encountered

**Time Complexity**: O(log n) average, O(n) worst case

### 3. Deletion Operation
**Purpose**: Remove a node from BST while preserving BST property

**Three Cases**:
1. **Leaf Node (No children)**: Simply remove the node
2. **One Child**: Replace node with its child
3. **Two Children**: Replace with inorder successor (or predecessor)
   - Find the smallest value in right subtree
   - Replace current node's value with successor's value
   - Delete the successor node

**Time Complexity**: O(log n) average, O(n) worst case

## Advanced Operations

### 1. Tree Traversals
- **Inorder**: Left → Root → Right (gives sorted sequence)
- **Preorder**: Root → Left → Right
- **Postorder**: Left → Right → Root

### 2. BST Validation
**Purpose**: Verify if a binary tree satisfies BST properties

**Approach**: Use range-based validation
- For each node, maintain valid range [min, max]
- Root can have any value: [-∞, +∞]
- Left child range: [min, parent_value)
- Right child range: (parent_value, max]

### 3. Range Queries
**Purpose**: Find all values within a given range [start, end]

**Algorithm**:
- If current value > start, explore left subtree
- If start ≤ current value ≤ end, include current value
- If current value < end, explore right subtree

### 4. Tree Balancing
**Purpose**: Convert an unbalanced BST to a balanced one

**Approach**:
1. Perform inorder traversal to get sorted array
2. Recursively build balanced BST from sorted array
3. Choose middle element as root for each subtree

### 5. Merging BSTs
**Purpose**: Combine two BSTs into a single balanced BST

**Algorithm**:
1. Get inorder traversals of both BSTs
2. Merge the sorted arrays
3. Build balanced BST from merged array

## Time Complexity Analysis

| Operation | Average Case | Worst Case | Best Case |
|-----------|--------------|------------|-----------|
| Search    | O(log n)     | O(n)       | O(1)      |
| Insert    | O(log n)     | O(n)       | O(1)      |
| Delete    | O(log n)     | O(n)       | O(1)      |
| Traversal | O(n)         | O(n)       | O(n)      |

### Space Complexity
- **Storage**: O(n) for n nodes
- **Recursion Stack**: O(log n) average, O(n) worst case

## Common Problems and Solutions

### 1. Skewed Trees Problem
**Issue**: When insertions are in sorted order, BST becomes a linked list
**Solution**: Use self-balancing trees (AVL, Red-Black) or periodic rebalancing

### 2. Finding Largest BST in Binary Tree
**Approach**: Bottom-up traversal tracking BST validity and size
**Key Insight**: A subtree is BST if both children are BSTs and value constraints are satisfied

### 3. Root-to-Leaf Paths
**Purpose**: Find all paths from root to leaf nodes
**Technique**: Backtracking with path maintenance

### 4. Inorder Successor/Predecessor
**Successor**: Next larger element in inorder traversal
**Predecessor**: Previous smaller element in inorder traversal

## Best Practices

### Code Design
1. **Consistent Node Structure**: Use consistent attribute names (val/value/key)
2. **Null Handling**: Always check for null nodes before operations
3. **Recursive vs Iterative**: Choose based on stack depth concerns

### Performance Optimization
1. **Balance Maintenance**: Periodically rebalance or use self-balancing variants
2. **Iterative Solutions**: Use for deep trees to avoid stack overflow
3. **Caching**: Store frequently accessed values like tree size

### Error Handling
1. **Edge Cases**: Handle empty trees, single nodes, duplicate values
2. **Validation**: Verify BST property before operations
3. **Boundary Conditions**: Check range limits in range queries

### Memory Management
1. **Node Cleanup**: Properly deallocate nodes during deletion
2. **Avoid Memory Leaks**: Be careful with recursive operations
3. **Path Copying**: Use path copying for thread safety when needed

## Implementation Tips

### Common Patterns
```python
# Standard recursive search pattern
def search(root, target):
    if not root or root.val == target:
        return root
    return search(root.left, target) if target < root.val else search(root.right, target)

# Inorder traversal pattern
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
```

### Validation Techniques
- Range-based validation for BST property
- Size tracking for balanced tree operations
- Parent pointers for bidirectional traversal (when needed)

## Conclusion

Binary Search Trees provide an elegant solution for maintaining sorted data with efficient operations. Understanding the fundamental properties and common algorithms is essential for solving complex tree-based problems. The key to mastering BSTs lies in understanding the recursive nature of the data structure and practicing various traversal and manipulation techniques.

Remember that while BSTs offer excellent average-case performance, their worst-case behavior (O(n)) occurs with skewed trees. In production systems, consider self-balancing variants like AVL trees or Red-Black trees for guaranteed logarithmic performance.
