def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    # Step 1: Calculate value/weight ratio and store as tuple (ratio, weight, value)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Step 2: Sort items in descending order by ratio
    items.sort(reverse=True)

    total_value = 0.0  # Maximum value accumulated
    for ratio, weight, value in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take the fractional part
            total_value += ratio * capacity
            break

    return total_value


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
