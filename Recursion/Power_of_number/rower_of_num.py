def power(a, b):
     
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 5))    


# Using Optimized approach  

def power(a, b):
    # Base case
    if b == 0:
        return 1
    
    # If exponent is even
    if b % 2 == 0:
        half = power(a, b // 2)
        return half * half
    else:  # If exponent is odd
        return a * power(a, b - 1)

 
print(power(2, 5))    
