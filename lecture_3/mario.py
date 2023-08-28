def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
    main()

# debugger:
# place breakpoint and open debugger
# step over - execute line, but not step into it
# step into - go into the function
# play - break out of breakpoint and continue code