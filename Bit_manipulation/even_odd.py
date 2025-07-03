def check_even_odd(num):
    if num & 1 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Test cases
check_even_odd(10)
check_even_odd(7)
check_even_odd(0)
check_even_odd(-3)
