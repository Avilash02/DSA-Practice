numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(numbers)
max_value = max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Alternative approach without using built-in functions
min_value = numbers[0]
max_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
print("Alternative Minimum value:", min_value)
print("Alternative Maximum value:", max_value)