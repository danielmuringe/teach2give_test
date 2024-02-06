"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
"""

text = input("Enter a sentence: ").lower()

vowels = "aeiou"

count = 0
for letter in text:
    if letter in vowels:
        count += 1


print(f"The number of vowels in the sentence is {count}")
