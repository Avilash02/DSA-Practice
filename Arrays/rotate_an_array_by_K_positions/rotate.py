def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # handle cases where k > n
    return arr[k:] + arr[:-k]  # slicing for rotation


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated = rotate_array(arr, k)
print("Original array:", arr)
print(f"Array after rotating by {k} positions:", rotated)
  
#  If you want left rotation instead of right rotation, just swap the slicing:
#  return arr[k:] + arr[:k]  # for left rotation
