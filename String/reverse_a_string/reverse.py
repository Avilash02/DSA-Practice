text = "hello"
reversed_text = ''.join(reversed(text))
print(reversed_text) 

# using slicing
reversed_text_slicing = text[::-1]
print(reversed_text_slicing)

# using for loop
reversed_text_loop = ''
for char in text:
    reversed_text_loop = char + reversed_text_loop
print(reversed_text_loop)

