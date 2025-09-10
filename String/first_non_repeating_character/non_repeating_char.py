def first_non_repeating_index(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i   # return index
    
    return -1  # if all are repeating

s = "swiss"
print("Index:", first_non_repeating_index(s))
print("Character:", s[first_non_repeating_index(s)])

#using collections
 
from collections import Counter

def first_non_repeating_index(s):
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

# Example
s = "programming"
idx = first_non_repeating_index(s)
if idx != -1:
    print("Index:", idx)
    print("Character:", s[idx])
else:
    print("All characters are repeating")

