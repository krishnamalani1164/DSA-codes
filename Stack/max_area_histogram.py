def max_histogram_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index+=1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * ((index - stack[-1]-1) if stack else index))
            max_area = max(max_area,area)
    
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] * ((index - stack[-1] -1)if stack else index))
        max_area = max(max_area,area)
    
    return max_area



histogram = [2, 1, 5, 6, 2, 3]
print("Maximum area:", max_histogram_area(histogram))