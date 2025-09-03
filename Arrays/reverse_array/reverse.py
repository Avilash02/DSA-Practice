#using slicing
original_string = "Hello, World!"
reversed_string = original_string[::-1]
print(reversed_string)

#using reversed function
reversed_string_string =  reversed(original_string)
print(reversed_string)

#using loops
reversed_string_loop = " "
for char in original_string:
    reversed_string_loop = char + reversed_string_loop
print(reversed_string)

#using recursion
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_recursion(s[:-1]) #OR revrse_recursion(s[1:]) + s[0]
print(reverse_recursion(original_string))

#using stack
def reverse_stack(s):
    stack = list(s)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return reversed_s
print(reverse_stack(original_string))

#using list reverse method
def reverse_list_method(s):
    char_list = list(s)
    char_list.reverse()
    return ' '.join(char_list)
print(reverse_list_method(original_string))

