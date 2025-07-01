# Greedy Algorithms

A comprehensive collection of greedy algorithm implementations in Python, demonstrating fundamental concepts and real-world applications.

## Table of Contents
- [What are Greedy Algorithms?](#what-are-greedy-algorithms)
- [Key Characteristics](#key-characteristics)
- [When to Use Greedy Algorithms](#when-to-use-greedy-algorithms)
- [Greedy Choice Property](#greedy-choice-property)
- [Optimal Substructure](#optimal-substructure)
- [Algorithm Analysis](#algorithm-analysis)
- [Implemented Algorithms](#implemented-algorithms)
- [Usage Examples](#usage-examples)
- [Complexity Analysis](#complexity-analysis)
- [Common Pitfalls](#common-pitfalls)

## What are Greedy Algorithms?

Greedy algorithms are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum. The term "greedy" refers to the algorithm's approach of making the best choice available at each moment without considering the consequences of that choice on future steps.

### Core Philosophy
The greedy approach follows the principle: **"Take what you can get now!"**

At each step, a greedy algorithm:
1. Makes a choice that looks best at the moment
2. Never reconsiders previous choices
3. Hopes that the sequence of locally optimal choices leads to a globally optimal solution

## Key Characteristics

### 1. **Irrevocable Decisions**
Once a greedy algorithm makes a choice, it never changes its mind. This is both a strength (efficiency) and a potential weakness (suboptimal solutions).

### 2. **Local Optimization**
At each step, the algorithm chooses the option that appears best according to some criterion, without considering the global picture.

### 3. **No Backtracking**
Unlike dynamic programming or backtracking algorithms, greedy algorithms don't explore alternative paths or reconsider previous decisions.

### 4. **Step-by-Step Construction**
The solution is built incrementally, one piece at a time.

## When to Use Greedy Algorithms

Greedy algorithms work well when a problem exhibits two key properties:

### 1. Greedy Choice Property
A globally optimal solution can be arrived at by making locally optimal (greedy) choices. This means the choice made by a greedy algorithm at each step is safe and will not prevent finding an optimal solution.

### 2. Optimal Substructure
An optimal solution to the problem contains optimal solutions to subproblems. This allows the problem to be solved by combining optimal solutions to smaller instances.

## Algorithm Design Process

1. **Cast the optimization problem** as one in which we make a choice and are left with one subproblem to solve
2. **Prove that there's always an optimal solution** that makes the greedy choice
3. **Demonstrate optimal substructure** by showing that having made the greedy choice, the remaining subproblem has the property that combining an optimal solution to the subproblem with the greedy choice yields an optimal solution to the original problem

## Implemented Algorithms

### 1. Activity Selection Problem (`activity_selection.py`)
**Problem**: Select the maximum number of non-overlapping activities from a set of activities with start and end times.

**Greedy Strategy**: Always pick the activity that finishes earliest among the remaining activities.

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(1)

### 2. Fractional Knapsack (`fractional_knapsack.py`)
**Problem**: Fill a knapsack with items to maximize value, where items can be taken in fractions.

**Greedy Strategy**: Sort items by value-to-weight ratio and take items with the highest ratio first.

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(n) for storing ratios

### 3. Indian Coin Change (`indian_coins.py`)
**Problem**: Make change for a given amount using the minimum number of coins from Indian denominations.

**Greedy Strategy**: Always use the largest denomination possible at each step.

**Time Complexity**: O(k) where k is the number of denominations
**Space Complexity**: O(1)

**Note**: This works optimally for Indian currency system due to its canonical nature.

### 4. Job Sequencing with Deadlines (`job_sequencing_oops.py`)
**Problem**: Schedule jobs with deadlines and profits to maximize total profit.

**Greedy Strategy**: Sort jobs by profit in descending order and schedule each job as late as possible before its deadline.

**Time Complexity**: O(n²) in worst case
**Space Complexity**: O(n)

### 5. Maximum Chain Length (`max_chain_length.py`)
**Problem**: Find the maximum length chain of pairs where each pair's first element is smaller than the next pair's first element.

**Greedy Strategy**: Sort pairs by their second element and greedily select pairs.

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(1)

### 6. Minimum Absolute Difference Pairs (`min_abs_diff.py`)
**Problem**: Find a pair of elements (one from each array) with minimum absolute difference.

**Greedy Strategy**: Sort both arrays and use two pointers to find the minimum difference.

**Time Complexity**: O(n log n + m log m) for sorting
**Space Complexity**: O(1)

## Usage Examples

### Running the Algorithms

```python
# Activity Selection
from activity_selection import max_activities
start = [1, 2, 0, 5, 8, 5]
end = [3, 5, 6, 9, 9, 7]
result = max_activities(start, end)
print(f"Maximum activities: {result}")

# Fractional Knapsack
from fractional_knapsack import fractional_knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = fractional_knapsack(weights, values, capacity)
print(f"Maximum value: {max_value}")

# Indian Coins
from indian_coins import indian_coins_greedy
amount = 2753
coins = indian_coins_greedy(amount)
print(f"Coins used: {coins}")
```

## Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Optimal? |
|-----------|----------------|------------------|----------|
| Activity Selection | O(n log n) | O(1) | ✅ Yes |
| Fractional Knapsack | O(n log n) | O(n) | ✅ Yes |
| Indian Coin Change | O(k) | O(1) | ✅ Yes* |
| Job Sequencing | O(n²) | O(n) | ✅ Yes |
| Max Chain Length | O(n log n) | O(1) | ✅ Yes |
| Min Absolute Difference | O(n log n) | O(1) | ✅ Yes |

*For canonical coin systems like Indian currency

## Advantages and Disadvantages

### Advantages ✅
- **Simple to understand and implement**
- **Efficient**: Usually have good time complexity
- **Memory efficient**: Often require minimal extra space
- **Fast execution**: No need to explore multiple possibilities

### Disadvantages ❌
- **Not always optimal**: May not work for all problems
- **Hard to prove correctness**: Requires mathematical proof
- **Limited applicability**: Only works when greedy choice property holds
- **No flexibility**: Cannot adapt if initial choices prove suboptimal

## Common Pitfalls

1. **Assuming greedy always works**: Not all optimization problems can be solved optimally with greedy algorithms
2. **Wrong greedy choice**: Choosing the wrong local optimization criterion
3. **Ignoring counterexamples**: Always test with edge cases
4. **Forgetting to prove optimality**: A working greedy algorithm isn't necessarily optimal

## Examples Where Greedy Fails

### 0/1 Knapsack Problem
Unlike fractional knapsack, the 0/1 knapsack (where items cannot be fractioned) cannot be solved optimally with a greedy approach.

### Longest Path Problem
Finding the longest path in a graph cannot be solved optimally with greedy algorithms.

## Testing and Verification

Each algorithm includes test cases and examples. To verify correctness:

1. **Test with known optimal solutions**
2. **Try edge cases** (empty inputs, single elements)
3. **Compare with brute force** for small inputs
4. **Analyze time and space complexity**

## Contributing

Feel free to contribute additional greedy algorithms or improvements to existing implementations. Please ensure:

- Code follows Python PEP 8 style guidelines
- Include comprehensive docstrings
- Add test cases for new algorithms
- Update this README with algorithm descriptions

## References

- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- "Algorithm Design" by Jon Kleinberg and Éva Tardos
- "Greedy Algorithms" - Stanford CS161 Course Notes

## License

This project is open source and available under the [MIT License](LICENSE).
