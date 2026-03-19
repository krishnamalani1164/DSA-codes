# 📚 Stack Data Structure - Complete Guide & Implementation

A comprehensive collection of stack implementations, algorithms, and problem-solving techniques in Python. This repository covers fundamental concepts, advanced operations, and common interview problems with detailed explanations.

## 📋 Table of Contents

- [Theory & Fundamentals](#theory--fundamentals)
- [Key Concepts & Patterns](#key-concepts--patterns)
- [Implementation Files](#implementation-files)
- [Problem-Solving Techniques](#problem-solving-techniques)
- [Time & Space Complexity](#time--space-complexity)
- [Common Stack Patterns](#common-stack-patterns)
- [Interview Problems](#interview-problems)

## 🧠 Theory & Fundamentals

### What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. Think of it like a stack of plates - you can only add or remove plates from the top.

### Core Operations

1. **Push**: Add element to the top
2. **Pop**: Remove element from the top
3. **Peek/Top**: View top element without removing
4. **isEmpty**: Check if stack is empty
5. **Size**: Get number of elements

### Real-World Applications

- **Function Call Management**: Call stack in programming languages
- **Undo Operations**: Text editors, browsers
- **Expression Evaluation**: Mathematical expressions, compilers
- **Backtracking Algorithms**: Maze solving, game AI
- **Memory Management**: Stack memory allocation

## 🎯 Key Concepts & Patterns

### 1. Monotonic Stack
**Use Cases**: Next greater element, stock span, histogram problems

**Pattern**:
```python
stack = []
for i in range(len(arr)):
    while stack and condition:  # condition varies by problem
        stack.pop()
    # Process current element
    stack.append(i)
```

### 2. Stack for Parentheses/Brackets
**Use Cases**: Valid parentheses, duplicate parentheses

**Pattern**:
```python
stack = []
for char in expression:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()
return len(stack) == 0
```

### 3. Stack for Recursion Simulation
**Use Cases**: Converting recursive solutions to iterative

### 4. Two-Stack Approach
**Use Cases**: Implementing queues, evaluating expressions

## 📁 Implementation Files

### Core Stack Implementations

#### `stack_using_list.py`
**Basic Stack using Python List**
- Simple implementation using built-in list
- O(1) average case for push/pop operations
- Dynamic resizing handled automatically

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")
```

#### `stack_using_linked_list.py`
**Stack using Linked List**
- More memory efficient for sparse usage
- O(1) guaranteed time complexity
- Dynamic memory allocation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
```

#### `stack_using_generic.py`
**Type-Safe Generic Stack**
- Uses Python typing for type safety
- Generic implementation supporting any data type
- Professional-grade implementation

### Classic Stack Problems

#### `valid_parenthesis.py`
**Balanced Parentheses Checker**
```python
def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif matches_pair(char, stack):
            stack.pop()
        else:
            return False
    return not stack
```
**Key Insight**: Use stack to match opening and closing brackets

#### `duplicate_paretheses.py`
**Duplicate Parentheses Detection**
- Detects redundant parentheses like `((a+b))`
- Uses stack to count elements between parentheses
- **Logic**: If no elements between `(` and `)`, it's duplicate

#### `next_greater_element.py`
**Next Greater Element (Monotonic Stack)**
```python
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result
```
**Key Pattern**: Monotonic decreasing stack, traverse right to left

#### `stock_span.py`
**Stock Span Problem**
- Calculate span of stock prices (consecutive days with price ≤ current)
- Uses monotonic stack to store indices
- **Insight**: Stack maintains indices in decreasing order of prices

#### `max_area_histogram.py`
**Largest Rectangle in Histogram**
```python
def max_histogram_area(heights):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = heights[top] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
    
    # Process remaining elements
    while stack:
        top = stack.pop()
        area = heights[top] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(max_area, area)
    
    return max_area
```
**Advanced Pattern**: Use stack to find left and right boundaries efficiently

### Recursive Operations

#### `reverse_string_using_stack.py`
**String Reversal**
- Simple demonstration of LIFO property
- Push all characters, then pop to get reverse

#### `push_at_bottom.py`
**Insert at Bottom of Stack**
```python
def push_at_bottom(stack, element):
    if not stack:
        stack.append(element)
    else:
        temp = stack.pop()
        push_at_bottom(stack, element)
        stack.append(temp)
```
**Recursive Pattern**: Use recursion to reach bottom, then build back up

#### `reverse_stack_recursion.py`
**Stack Reversal using Recursion**
- Combines recursion with push_at_bottom
- Demonstrates advanced recursive thinking
- O(n²) time complexity due to nested recursion

## 🚀 Problem-Solving Techniques

### Pattern Recognition Guide

| Problem Type | Key Indicators | Technique | Example |
|-------------|----------------|-----------|---------|
| **Parentheses Problems** | Brackets, matching pairs | Stack for pairing | `valid_parenthesis.py` |
| **Next Greater/Smaller** | Find next larger/smaller element | Monotonic Stack | `next_greater_element.py` |
| **Histogram/Area Problems** | Find largest rectangle/area | Stack with indices | `max_area_histogram.py` |
| **Span Problems** | Count consecutive elements | Stack with indices | `stock_span.py` |
| **Expression Evaluation** | Mathematical expressions | Multiple stacks | Advanced topic |
| **Recursive to Iterative** | Convert recursion | Stack simulation | `reverse_stack_recursion.py` |

### Step-by-Step Problem Solving

1. **Identify the Pattern**
   - What needs to be remembered?
   - Is there a matching/pairing requirement?
   - Do we need to find next/previous elements?

2. **Choose Stack Strategy**
   - **Simple Stack**: For basic LIFO operations
   - **Monotonic Stack**: For next greater/smaller problems
   - **Stack with Indices**: When position matters
   - **Multiple Stacks**: For complex state management

3. **Handle Edge Cases**
   - Empty stack operations
   - Single element
   - All elements same
   - Stack overflow (in limited memory scenarios)

4. **Optimize**
   - Can we reduce space complexity?
   - Is one pass sufficient?
   - Can we avoid extra data structures?

## ⏱️ Time & Space Complexity

### Basic Operations

| Operation | Array-based | Linked List-based |
|-----------|-------------|-------------------|
| Push | O(1) amortized* | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Search | O(n) | O(n) |
| Space | O(n) | O(n) + pointer overhead |

*O(1) amortized due to dynamic array resizing

### Algorithm Complexities

| Algorithm | Time | Space | File |
|-----------|------|-------|------|
| Valid Parentheses | O(n) | O(n) | `valid_parenthesis.py` |
| Next Greater Element | O(n) | O(n) | `next_greater_element.py` |
| Stock Span | O(n) | O(n) | `stock_span.py` |
| Max Histogram Area | O(n) | O(n) | `max_area_histogram.py` |
| Stack Reversal (Recursive) | O(n²) | O(n) | `reverse_stack_recursion.py` |

## 🔄 Common Stack Patterns

### 1. Monotonic Stack Pattern
```python
# For Next Greater Element type problems
def monotonic_stack_template(arr):
    stack = []
    result = []
    
    for i in range(len(arr)):
        while stack and condition(arr[stack[-1]], arr[i]):
            index = stack.pop()
            result[index] = arr[i]  # or some computation
        stack.append(i)
    
    return result
```

### 2. Bracket Matching Pattern
```python
def bracket_matching_template(expression):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack[-1]] != char:
                return False
            stack.pop()
    
    return len(stack) == 0
```

### 3. Recursive Simulation Pattern
```python
def recursive_to_iterative_template():
    stack = [(initial_state)]
    
    while stack:
        current_state = stack.pop()
        
        if base_case(current_state):
            process_base_case(current_state)
        else:
            # Push subproblems in reverse order
            for subproblem in reversed(get_subproblems(current_state)):
                stack.append(subproblem)
```

## 🎯 Interview Problems Checklist

### Must-Know Problems ⭐
- [ ] Valid Parentheses
- [ ] Next Greater Element
- [ ] Largest Rectangle in Histogram
- [ ] Implement Stack using Queues
- [ ] Min Stack (stack that supports getMin in O(1))
- [ ] Evaluate Reverse Polish Notation

### Advanced Problems ⭐⭐
- [ ] Trapping Rain Water
- [ ] Remove K Digits
- [ ] 132 Pattern
- [ ] Asteroid Collision
- [ ] Daily Temperatures
- [ ] Sum of Subarray Minimums

### Expert Level ⭐⭐⭐
- [ ] Maximum Rectangle in Binary Matrix
- [ ] Sliding Window Maximum
- [ ] Basic Calculator I, II, III
- [ ] Expression Add Operators

## 💡 Pro Tips & Common Pitfalls

### Pro Tips

1. **Visualize the Stack**: Always draw the stack state while solving
2. **Think Backwards**: Many problems are easier when processed right-to-left
3. **Use Indices**: Store indices instead of values when position matters
4. **Monotonic Stacks**: Master this pattern - it appears frequently
5. **Edge Cases**: Always consider empty stack, single element, duplicates

### Common Pitfalls

1. **Empty Stack Check**
   ```python
   # Bad
   top = stack.pop()
   
   # Good
   if stack:
       top = stack.pop()
   ```

2. **Index vs Value Confusion**
   ```python
   # Be clear about what you're storing
   stack.append(i)        # storing index
   stack.append(arr[i])   # storing value
   ```

3. **Forgetting to Push Current Element**
   ```python
   # Common mistake in monotonic stack
   while stack and condition:
       stack.pop()
   # Don't forget this!
   stack.append(current)
   ```

## 🔧 Usage Examples

```python
# Basic stack operations
from stack_using_list import Stack

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20

# Parentheses validation
from valid_parenthesis import is_valid_parentheses
print(is_valid_parentheses("()[]{}"))  # Output: True

# Next greater element
from next_greater_element import next_greater_element
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]

# Histogram area
from max_area_histogram import max_histogram_area
heights = [2, 1, 5, 6, 2, 3]
print(max_histogram_area(heights))  # Output: 10
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Add your implementation with proper documentation
4. Include test cases and complexity analysis
5. Submit a pull request

## 📚 Further Reading

- [GeeksforGeeks - Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/)
- [LeetCode - Stack Problems](https://leetcode.com/tag/stack/)
- [Monotonic Stack Pattern](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)

---

**Happy Coding! 🚀**

*Master the stack by understanding when and why to use it, not just how to implement it.*
