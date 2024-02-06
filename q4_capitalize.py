"""
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
"""

text = f' {input("Enter a string: ")} '


upp = lambda char: chr(ord(char) - 32)  # Convert lowercase to uppercase

i = 0
while i < len(text):
    char = text[i]

    if char == " " and i < (len(text) - 1):
        next_char = text[i + 1]
        ord_next_char = ord(next_char)

        if 97 <= ord_next_char <= 122:
            text = text[: i + 1] + upp(next_char) + text[i + 2 :]

    i += 1

print(text)
