def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter how many terms: "))
print("Fibonacci Series:", [fibonacci(i) for i in range(n)])
