"""
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
"""

text = f' {input("Enter a string: ")} '


# Convert character in a certain index to uppercase
upp = lambda i, text: f"{text[: i + 1]}{chr(ord(text[i + 1]) - 32)}{text[i + 2 :]}"

# Ensure current character is a space and the next char is a lowercase
conds = lambda i, text: (text[i] == " ") and (97 <= ord(text[i + 1]) <= 122)

i = 0
while i < (len(text) - 1):

    if conds(i, text):
        text = upp(i, text)  # Capitalize the next character

    i += 1

print(text)
