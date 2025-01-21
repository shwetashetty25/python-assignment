#5.Write a Python program that asks the user to input a float number, then prints the integer part (truncate), and the fraction part separately.
number = float(input("Enter a float number: "))
integer_part = int(number)
fraction_part = number - integer_part
print(f"Integer part: {integer_part}")
print(f"Fractional part: {fraction_part}")
