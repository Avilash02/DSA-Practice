#  If Only ONE Number Is Missing

def find_missing_number(arr):
    n = len(arr) + 1  # because one number is missing
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 4, 5, 6]  
print("Missing number:", find_missing_number(arr))


# If More Than ONE Number Is Missing

def find_missing_numbers(arrr):
    n = max(arrr)  # or use expected n if known
    full_set = set(range(1, n + 1))
    missing = full_set - set(arrr)
    return sorted(list(missing))

arrr = [1, 2, 6]
print("Missing numbers:", find_missing_numbers(arrr))   
