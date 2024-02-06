"""
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two
"""

from math import log2


num = int(input("Enter a number: "))
log_num = log2(num)


if num.is_float():
    print(log_num and log_num.is_integer())
else:
    print("Invalid input")
