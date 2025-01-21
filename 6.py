#6.Write a Python function that takes a string and returns its length without using the built-in len() function.
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
user_input = input("Enter a string: ")
print(f"The length of the string is: {string_length(user_input)}")