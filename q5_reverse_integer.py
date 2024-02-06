"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
"""

num = input("Enter a number: ")

sign = ""
if num[0] == "-":  # if the number is negative
    num = num[1:]
    sign = "-"

if num.isdigit():
    num = num.lstrip("0")
    print(f"The reversed number is {sign}{num[::-1].lstrip('0')}")
else:
    print("Invalid input")
