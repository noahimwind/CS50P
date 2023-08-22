# use "code name.py" to create python file
# use "python name.py" to execute file

def main():
    # get input from user
    name = input("What is your name? ")
    # name = input("What is your name?").strip().title()
    hello(name)

def hello(adressee = "stranger"):
    print(f"Hello, {adressee}")

main()

# first, last = name.split(" ")
# print(f"Hello, {first}.") # print is a function that takes arguments
