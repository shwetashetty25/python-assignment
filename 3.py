#3.Write a Python program that prompts the user for two numbers and prints their sum, difference, product, and quotient.
# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (division by zero is not allowed)"
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
