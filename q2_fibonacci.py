"""
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100
"""

sequence = [0, 1]  # Sequence of numbers
pairs = [0, 1]  # Last two numbers in the sequence

while True:
    next_number = pairs[0] + pairs[1]

    # Break if the next number is greater than 100
    if next_number > 100:
        break

    pairs[0] = pairs[1]
    pairs[1] = next_number

    # Ensure there is no duplicate of 0 or 1
    if next_number <= 1:
        continue

    sequence.append(next_number)


print(sequence)
