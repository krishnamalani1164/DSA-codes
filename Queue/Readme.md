# Queue Data Structure - Complete Implementation Guide

## Table of Contents
- [Introduction](#introduction)
- [Queue Theory](#queue-theory)
- [Implementations](#implementations)
- [Key Concepts](#key-concepts)
- [Problem Solving Patterns](#problem-solving-patterns)
- [File Descriptions](#file-descriptions)
- [Usage Examples](#usage-examples)
- [Time and Space Complexity](#time-and-space-complexity)
- [Advanced Topics](#advanced-topics)

## Introduction

This repository contains comprehensive implementations of the Queue data structure in Python, including various types of queues, queue-based algorithms, and practical applications. A queue follows the **FIFO (First In, First Out)** principle, making it essential for many real-world applications.

## Queue Theory

### What is a Queue?
A queue is a linear data structure that follows the FIFO principle:
- **Enqueue**: Add elements to the rear/back
- **Dequeue**: Remove elements from the front
- **Front/Peek**: View the front element without removing it

### Real-World Applications
- **Process Scheduling**: Operating systems use queues to manage processes
- **Breadth-First Search (BFS)**: Graph traversal algorithms
- **Buffer Management**: Data streams, I/O operations
- **Print Queue**: Managing print jobs
- **Call Center Systems**: Managing customer calls

## Implementations

### 1. Array-Based Queue
- **Fixed Size**: Predetermined capacity
- **Linear Implementation**: Simple but inefficient due to shifting elements
- **Memory Efficient**: Contiguous memory allocation

### 2. Circular Queue
- **Wrap-Around**: Uses modular arithmetic to reuse empty spaces
- **Space Efficient**: No memory wastage
- **Fixed Size**: Predetermined capacity
- **Key Formula**: `next_index = (current_index + 1) % size`

### 3. Linked List Queue
- **Dynamic Size**: Grows and shrinks as needed
- **Memory Efficient**: Only allocates memory when needed
- **No Size Limit**: Limited only by available memory

### 4. Deque (Double-Ended Queue)
- **Bidirectional**: Insert/remove from both ends
- **Versatile**: Can function as both stack and queue
- **Python Built-in**: `collections.deque` provides optimized implementation

## Key Concepts

### 1. Queue Operations
```python
# Basic Operations
enqueue(item)    # Add to rear - O(1)
dequeue()        # Remove from front - O(1)
peek()/front()   # View front element - O(1)
is_empty()       # Check if empty - O(1)
size()           # Get queue size - O(1)
```

### 2. Circular Queue Logic
```python
# Key conditions for circular queue
is_full = (rear + 1) % size == front
is_empty = front == -1
next_rear = (rear + 1) % size
next_front = (front + 1) % size
```

### 3. Queue State Management
- **Empty State**: `front == -1` or `front > rear`
- **Full State**: `(rear + 1) % size == front` (circular)
- **Single Element**: `front == rear`

## Problem Solving Patterns

### 1. **Sliding Window with Queue**
- Use deque for efficient front/rear operations
- Maintain window size by removing elements from front
- Example: First non-repeating character in stream

### 2. **Interleaving/Merging**
- Process multiple queues simultaneously
- Alternate between queues for fair processing
- Example: Interleaving two queues

### 3. **Queue Reversal**
- Use auxiliary stack to reverse queue order
- Dequeue all → Push to stack → Pop from stack → Enqueue back
- Time: O(n), Space: O(n)

### 4. **Data Structure Conversion**
- **Queue using Stacks**: Use two stacks for FIFO behavior
- **Stack using Queues**: Use two queues for LIFO behavior
- Demonstrates understanding of both data structures

### 5. **Stream Processing**
- Process continuous data streams
- Maintain state using queue
- Example: Character frequency tracking

## File Descriptions

### Core Implementations
- **`circular_queue_array.py`**: Circular queue using array with wrap-around logic
- **`linked_list_queue.py`**: Dynamic queue using linked list nodes
- **`queue_as_dequeue.py`**: Queue implementation using Python's deque
- **`deque.py`**: Basic deque operations demonstration

### Advanced Applications
- **`first_non_repeating_character.py`**: Stream processing with frequency tracking
- **`interleave_queue.py`**: Merging multiple queues fairly
- **`queue_reversal.py`**: Reversing queue using stack

### Data Structure Conversions
- **`queue_using_stack.py`**: Implementing queue using two stacks
- **`stack_using_queue.py`**: Implementing stack using two queues
- **`stack_using_deque.py`**: Stack implementation using deque

## Usage Examples

### Basic Queue Operations
```python
from collections import deque

# Create queue
q = deque()

# Enqueue elements
q.append(10)    # Add to rear
q.append(20)
q.append(30)

# Dequeue elements
front = q.popleft()  # Remove from front
print(front)  # Output: 10
```

### Circular Queue
```python
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
print(cq.dequeue())  # Output: 1
```

### Problem Solving
```python
# First non-repeating character
def first_non_repeating(stream):
    freq = {}
    q = deque()
    
    for char in stream:
        freq[char] = freq.get(char, 0) + 1
        q.append(char)
        
        while q and freq[q[0]] > 1:
            q.popleft()
        
        result = q[0] if q else None
        print(f"First non-repeating: {result}")
```

## Time and Space Complexity

### Basic Operations
| Operation | Array Queue | Circular Queue | Linked List Queue | Deque |
|-----------|-------------|----------------|-------------------|-------|
| Enqueue   | O(1)        | O(1)           | O(1)              | O(1)  |
| Dequeue   | O(n)*       | O(1)           | O(1)              | O(1)  |
| Peek      | O(1)        | O(1)           | O(1)              | O(1)  |
| Space     | O(n)        | O(n)           | O(n)              | O(n)  |

*Linear array queue requires O(n) for dequeue due to shifting elements

### Problem Complexities
- **Queue Reversal**: Time O(n), Space O(n)
- **Interleaving**: Time O(n), Space O(1)
- **First Non-Repeating**: Time O(n), Space O(k) where k is unique characters

## Advanced Topics

### 1. **Priority Queue**
- Elements have priority values
- Higher priority elements dequeued first
- Implementation using heaps

### 2. **Concurrent Queues**
- Thread-safe operations
- Multiple producers/consumers
- Lock-free implementations

### 3. **Bounded vs Unbounded Queues**
- **Bounded**: Fixed maximum size
- **Unbounded**: Grows as needed
- Memory management considerations

### 4. **Queue Applications in Algorithms**
- **BFS Traversal**: Level-order tree/graph traversal
- **Topological Sorting**: Kahn's algorithm
- **Shortest Path**: Dijkstra's algorithm with priority queue

## Key Problem-Solving Tips

1. **Choose Right Implementation**:
   - Use deque for most applications
   - Use circular queue for fixed-size requirements
   - Use linked list for dynamic sizing

2. **Common Patterns**:
   - **Two-pointer technique**: Use with deque for sliding window
   - **Auxiliary data structures**: Combine with stack/hash for complex problems
   - **State tracking**: Maintain additional information alongside queue

3. **Edge Cases**:
   - Empty queue operations
   - Full queue operations (bounded queues)
   - Single element scenarios
   - Memory constraints

4. **Optimization Strategies**:
   - Use deque over list for frequent front operations
   - Consider space-time tradeoffs
   - Batch operations when possible

## Getting Started

1. Clone the repository
2. Run individual Python files to see implementations
3. Modify examples to understand behavior
4. Practice with different problem variations

## Contributing

Feel free to add more queue implementations, algorithms, or optimizations. Ensure code follows Python best practices and includes proper documentation.

---

*This repository serves as a comprehensive guide to understanding and implementing queue data structures and their applications in problem-solving.*
