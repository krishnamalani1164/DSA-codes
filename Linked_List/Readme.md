# 🔗 Linked List Data Structure - Complete Guide & Implementation

A comprehensive collection of linked list implementations, algorithms, and problem-solving techniques in Python. This repository covers fundamental concepts, advanced operations, and common interview problems with detailed explanations.

## 📚 Table of Contents

- [Theory & Fundamentals](#theory--fundamentals)
- [Key Concepts & Patterns](#key-concepts--patterns)
- [Implementation Files](#implementation-files)
- [Problem-Solving Techniques](#problem-solving-techniques)
- [Time & Space Complexity](#time--space-complexity)
- [Common Pitfalls & Tips](#common-pitfalls--tips)

## 🧠 Theory & Fundamentals

### What is a Linked List?

A **Linked List** is a linear data structure where elements (nodes) are stored in sequence, but unlike arrays, elements are not stored in contiguous memory locations. Each node contains:
- **Data**: The actual value
- **Next**: Reference/pointer to the next node

### Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node
2. **Doubly Linked List**: Each node has pointers to both next and previous nodes
3. **Circular Linked List**: Last node points back to the first node

### Advantages
- Dynamic size (grows/shrinks during runtime)
- Efficient insertion/deletion at the beginning (O(1))
- Memory efficient (allocates memory as needed)

### Disadvantages
- No random access (must traverse from head)
- Extra memory overhead for storing pointers
- Not cache-friendly due to non-contiguous memory

## 🎯 Key Concepts & Patterns

### 1. Two Pointer Technique
**Use Cases**: Cycle detection, finding middle, nth node from end

**Pattern**:
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next        # Move 1 step
    fast = fast.next.next   # Move 2 steps
```

### 2. Floyd's Cycle Detection (Tortoise & Hare)
**Logic**: If there's a cycle, fast pointer will eventually meet slow pointer

### 3. Dummy Node Technique
**Use Cases**: Simplifying edge cases in insertion/deletion
```python
dummy = Node(0)
dummy.next = head
# Perform operations
return dummy.next
```

### 4. Recursive Approach
**Use Cases**: Reversing, merging, tree-like operations

### 5. Multiple Pass Strategy
**Use Cases**: When you need to know list length or perform complex operations

## 📁 Implementation Files

### Core Implementations

#### `linkedlist.py`
**Complete Singly Linked List Implementation**
- Basic operations: push_front, push_back, pop_front, pop_back
- Advanced: insert_at_position, delete_node
- Maintains both head and tail pointers for O(1) back operations

#### `doubly_ll.py`
**Doubly Linked List Implementation**
- Bi-directional traversal
- More memory per node but easier deletion
- Maintains previous pointers

#### `linked_list_library.py`
**Using Python's Built-in Collections**
- Demonstrates `collections.deque` as a doubly-linked list
- Built-in optimized operations

### Advanced Algorithms

#### `detect_a_cycle.py`
**Floyd's Cycle Detection Algorithm**
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Key Insight**: Fast pointer moves 2x speed, will lap slow pointer if cycle exists

#### `remove_a_cycle.py`
**Cycle Removal Algorithm**
1. **Detect** cycle using Floyd's algorithm
2. **Find** cycle start by moving one pointer to head
3. **Remove** cycle by breaking the link

#### `reverse_list.py`
**Iterative List Reversal**
```python
def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```

#### `merge_sort_ll.py`
**Merge Sort on Linked Lists**
- **Divide**: Find middle and split
- **Conquer**: Recursively sort both halves
- **Combine**: Merge sorted lists
- **Advantage**: O(1) space complexity (in-place)

#### `remove_nth_node.py`
**Remove Nth Node from End**
- Uses two-pointer technique with n+1 gap
- Single pass solution

#### `zig_zag_ll.py`
**Zigzag Reordering (1→2→3→4→5 becomes 1→5→2→4→3)**
1. Find middle
2. Reverse second half
3. Merge alternately

## 🚀 Problem-Solving Techniques

### Pattern Recognition

| Problem Type | Technique | Example |
|-------------|-----------|---------|
| Cycle Detection | Two Pointers (Floyd's) | `detect_a_cycle.py` |
| Find Middle | Slow/Fast Pointers | `merge_sort_ll.py` |
| Remove from End | Two Pointers with Gap | `remove_nth_node.py` |
| Reversal | Three Pointers | `reverse_list.py` |
| Merging | Dummy Node | `merge_sort_ll.py` |
| Reordering | Split + Reverse + Merge | `zig_zag_ll.py` |

### Common Problem-Solving Steps

1. **Understand the Problem**
   - What's the input/output?
   - Any constraints?
   - Edge cases?

2. **Choose the Right Technique**
   - Single pass vs multiple pass
   - Iterative vs recursive
   - Extra space vs in-place

3. **Handle Edge Cases**
   - Empty list
   - Single node
   - All nodes satisfy condition

4. **Optimize**
   - Can we do it in one pass?
   - Can we reduce space complexity?

## ⏱️ Time & Space Complexity

### Basic Operations

| Operation | Singly LL | Doubly LL | Array |
|-----------|-----------|-----------|-------|
| Access | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Insert (beginning) | O(1) | O(1) | O(n) |
| Insert (end) | O(1)* | O(1) | O(1) |
| Delete (beginning) | O(1) | O(1) | O(n) |
| Delete (end) | O(n) | O(1) | O(1) |

*O(1) if tail pointer is maintained

### Algorithm Complexities

| Algorithm | Time | Space | File |
|-----------|------|-------|------|
| Cycle Detection | O(n) | O(1) | `detect_a_cycle.py` |
| List Reversal | O(n) | O(1) | `reverse_list.py` |
| Merge Sort | O(n log n) | O(1) | `merge_sort_ll.py` |
| Remove Nth from End | O(n) | O(1) | `remove_nth_node.py` |

## ⚠️ Common Pitfalls & Tips

### Pitfalls to Avoid

1. **Null Pointer Exceptions**
   ```python
   # Bad
   if head.next.val == target:
   
   # Good
   if head and head.next and head.next.val == target:
   ```

2. **Losing References**
   ```python
   # Bad - loses reference to original next
   current.next = new_node
   
   # Good - save reference first
   temp = current.next
   current.next = new_node
   new_node.next = temp
   ```

3. **Not Updating Tail Pointer**
   - Always update tail when adding to end
   - Set tail to None when list becomes empty

### Pro Tips

1. **Use Dummy Nodes** for complex insertions/deletions
2. **Draw Diagrams** to visualize pointer movements
3. **Test Edge Cases**: empty list, single node, all nodes
4. **Consider Multiple Approaches**: iterative vs recursive
5. **Practice Pointer Manipulation** - it's the core skill

## 🎯 Interview Preparation

### Must-Know Problems
- [ ] Reverse a linked list
- [ ] Detect cycle in linked list
- [ ] Find middle of linked list
- [ ] Merge two sorted lists
- [ ] Remove nth node from end
- [ ] Check if linked list is palindrome
- [ ] Add two numbers represented as linked lists

### Advanced Problems
- [ ] Merge k sorted lists
- [ ] Copy list with random pointer
- [ ] LRU Cache implementation
- [ ] Flatten multilevel doubly linked list

## 🔧 Usage Examples

```python
# Basic usage
from linkedlist import LinkedList

ll = LinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.print_list()  # Output: 1 2 3

# Cycle detection
from detect_a_cycle import hasCycle
result = hasCycle(head)  # Returns True/False

# List reversal
from reverse_list import LinkedList
ll = LinkedList()
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)
ll.reverse()
ll.print_list()  # Output: 3 2 1
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your implementation with proper documentation
4. Include test cases and complexity analysis
5. Submit a pull request

## 📖 Further Reading

- [GeeksforGeeks - Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [LeetCode - Linked List Problems](https://leetcode.com/tag/linked-list/)
- [Cracking the Coding Interview - Chapter 2](https://www.crackingthecodinginterview.com/)

---

**Happy Coding! 🚀**

*Master linked lists by understanding the patterns, not just memorizing solutions.*
