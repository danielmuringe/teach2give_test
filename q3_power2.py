"""
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two
"""

num_input = input("Enter a number: ")


# Ensure its a integer number
if (not num_input.isdigit()) or ("." in num_input):
    print("Invalid input: Must be a positive integer number")
    exit()

num = int(num_input)
print(num & (num - 1) == 0 and num != 0)  # Do bitwise AND operation and compare with 0
