def calculate_span(prices):
    #Stack to store indices of elements
    stack = []
    span = [0] * len(prices)

    for i in range(len(prices)):
        #Pop elements from the stack while stack is not empty ans
        # the price at current index is greater than the price at the top of the stack
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

        #If stack is empty ,all previous prices are smaller
        #Otherwise calculate the span from the current index
        span[i] = i+1 if not stack else i - stack[-1]

        stack.append(i)

    return span

#Example Usage
prices = [100,80,60,70,60,85,100]
span = calculate_span(prices)
print("Stock Prices:",prices)
print("Span Values:",span)