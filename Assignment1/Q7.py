'''7.	Write a program to find all numbers between 1000 and 2500 (inclusive) that are divisible by 9 but not by 6. 
Extend the program so that the range limits (1000 and 2500) can also be entered by the user. '''

print("Displaying numbers between 1000 and 2500 (inclusive) that are divisible by 9 but not by 6.")

for num in range(1000, 2500 + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num, end=" ")


print("\nNow, Displaying all numbers between a user-defined range")

# Taking input for the range
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Finding numbers divisible by 9 but not by 6
print(f"Numbers between {lower} and {upper} divisible by 9 but not by 6:")

# Displaying the results
for num in range(lower, upper + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num, end=" ")
