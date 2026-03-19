def reverse_string_using_stack(string):

    stack = []

    for char in string:
        stack.append(char)
    
    reversed_string = ""

    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

input_string = "hello"
reversed_result = reverse_string_using_stack(input_string)
print(reversed_result)