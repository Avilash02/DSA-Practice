def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

arr = [4, 5, 6, 7, 4, 8, 5, 9, 6]
print("Duplicate elements using set:", find_duplicates(arr))

# using dictionary
def find_duplicates_dict(arr):
    count = {}
    duplicates = []
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, cnt in count.items():
        if cnt > 1:
            duplicates.append(num)
    
    return duplicates
print("Duplicate elements using dictionary:", find_duplicates_dict(arr))

#using mathematical formula
def find_duplicate_math(arr):
    n = len(arr) - 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return actual_sum - expected_sum
print("Duplicate element using mathematical formula:", find_duplicate_math(arr))
