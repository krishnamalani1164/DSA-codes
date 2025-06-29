def is_valid_parentheses(s):
    stack = [] #Initalize an empty stack

    for char in s:
        if char in "({[":
            stack.append(char) #Push opening parenthesis into the stack
        elif(char ==')' and stack and stack[-1]=='(') or \
        (char == '}' and stack and stack[-1]=='{') or \
        (char == ']' and stack and stack[-1]=='['):
            stack.pop() #Pop the opening parenthesis from the stack
        else:
            return False
        
    return not stack #Return True if the stack is empty, False otherwise

print(is_valid_parentheses("()"))       # Output: True
print(is_valid_parentheses("([{}])"))   # Output: True
print(is_valid_parentheses("(]"))       # Output: False
print(is_valid_parentheses("([)]"))     # Output: False
print(is_valid_parentheses("{[]}"))     # Output: True
