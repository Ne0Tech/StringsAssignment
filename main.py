user_input = input("Enter a string: ")

modified_string = user_input.upper()

modified_string = modified_string.replace(" ", "_")

print(modified_string)

print(len(modified_string))




user_input = input("Enter a string: ")

processed_string = user_input.replace(" ", "").lower()

is_palindrome = processed_string == processed_string[::-1]

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")