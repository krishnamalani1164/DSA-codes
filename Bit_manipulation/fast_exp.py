def fast_exp(a, b):
    if b == 0:
        return 1
    half = fast_exp(a, b // 2)
    if b % 2 == 0:
        return half * half
    else:
        return a * half * half
    
    
print(fast_exp(2, 10))         # 1024