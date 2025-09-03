def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

#OR return text == ''.join(reversed(text))

 
print("Palindrome Checker")
print("=" * 40)
 
 
while True:
    user_input = input("\nEnter text to check (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    
    if user_input.strip():
        result =  is_palindrome(user_input)
        if result:
            print(f'"{user_input}" is a palindrome.')
        else:
            print(f'"{user_input}" is not a palindrome.')
    else:
        print("Please enter some text.")

print("Goodbye!")