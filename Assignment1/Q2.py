'''2.	Write a program to take two integer inputs from the user and display the results of the following operations in a clean format
I. Addition
II. Multiplication
III. Division
IV. Modulus (remainder)
V. Exponentiation'''


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2: .2f}")
print(f"Modulus (remainder): {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")