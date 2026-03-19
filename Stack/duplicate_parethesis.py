def has_duplicate_parentheses(expression):
    stack = []

    for char in expression:
        if char == ')':
            top = stack.pop()
            elements_inside = 0

            while top != '(':
                elements_inside += 1
                top = stack.pop()
            
            if elements_inside == 0:
                return True
            
        else:
            stack.append(char)
        
    return False
# Example usage
expression = "((a+b)) + c"
if has_duplicate_parentheses(expression):
    print("The expression has duplicate parentheses.")
else:
    print("The expression does not have duplicate parentheses.")