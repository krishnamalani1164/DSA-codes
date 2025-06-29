def next_greater_element(arr):
    #Stack to keep track of Elements
    stack = []
    #Array to store the results
    result = [-1]*len(arr)
    #Traverse the array from right to left
    for i in range(len(arr)-1,-1,-1):
        #Pop elements from the stack that are less than or equalt o arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        #If the stack is not empty,the top element is the next greater element
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

arr = [4, 5, 2, 10, 8]
print("Input Array:", arr)
print("Next Greater Element:", next_greater_element(arr))
