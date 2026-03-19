def insert_at_bottom(stack,item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack,item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack,temp)

#Example Usage:
stack = [1,2,3,4]
print("Original Stack:",stack)
reverse_stack(stack)
print("Reversed Stack:",stack)