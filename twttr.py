# implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

text = input("Tweet someting: ")

for char in text:
    if char not in vowels:
        print(char, end="")