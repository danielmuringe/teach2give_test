"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
"""

sentence = input("Enter a sentence: ")
vowels = "aeiou"

count = 0
for letter in sentence.lower():
    if letter in vowels:
        count += 1


print(f"In the sentence:  '{sentence}'\nThere are {count} vowels")
