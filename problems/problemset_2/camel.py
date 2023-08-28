# implement a program that prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case

def main():
    camel_case = input("camel case: ")
    snake_case(camel_case)

def snake_case(text):
    for char in text:
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")

main()
