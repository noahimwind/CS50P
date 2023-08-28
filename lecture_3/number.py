def main():
    x = get_int("Whats x? ")
    print(x)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("your input is not a number")
            # pass ohne else dann
        else:  
            break
    return x

main()