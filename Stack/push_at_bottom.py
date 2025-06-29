def push_at_bottom(stack,element):
    if not stack:#Baase Case for recursive call
        stack.append(element)
    else:
        temp = stack.pop()#Pop the top element
        push_at_bottom(stack,element)#Recursive Call
        stack.append(temp)#Push the top element back

stack = [1,2,3]
push_at_bottom(stack,0)
print(stack)