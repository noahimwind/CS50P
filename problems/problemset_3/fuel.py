# implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    fuel_gauge()

def fuel_gauge():
    while True:
        try:
            fraction_input = input("Input your Fraction: ")
            x, y = fraction_input.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                raise InvalidFuel
        except (ValueError, InvalidFuel) as error:
            pass
        else:
            try:
                percentage = round((x / y) * 100)
            except ZeroDivisionError:
                pass
            else:
                if percentage >= 99:
                    print("F")
                elif percentage <= 1:
                    print("E")
                else:
                    print(f"{percentage}%")
                break

class InvalidFuel(Exception):
    "Raised when the input value is more than 100%"

if __name__ == "__main__":
    main()