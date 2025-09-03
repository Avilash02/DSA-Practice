#Done using recursion, iterative method and math module

def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("Factorial Calculator")
    print("=" * 30)

    while True:
        try:
             
            user_input = input("\n  Enter a number to calculate factorial (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("byeee!")
                break
          
            n = int(user_input)
            
           
            result_iter = factorial_iterative(n)
            result_recur = factorial_recursive(n)
            
            print(f"\n{n}! = Iterative: {result_iter}")
            print(f"{n}! = Recursive: {result_recur}")
            
            
            if n >= 0:
                import math
                math_result = math.factorial(n)
                print(f"{n}! = Math module: {math_result}")
                

        except ValueError:
            print("Please enter a valid integer!")
        except Exception as e:
            print(f"An error occurred: {e}")

 
if __name__ == "__main__":
    main()