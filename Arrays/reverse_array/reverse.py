def reverse_slicing(arr):
    return arr[::-1]

#  Using  reverse()
def reverse_builtin(arr):
    arr_copy = arr[:]   # make a copy to avoid modifying original
    arr_copy.reverse()
    return arr_copy

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed using slicing:", reverse_slicing(arr))
print("Reversed using  reverse():", reverse_builtin(arr))