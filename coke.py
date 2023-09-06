# implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

valid_coins = [25, 10, 5]

rem_cost = 50

while True:
    print(f"Amount Due: {rem_cost}")
    coin = int(input("Insert Coin: "))
    if coin in valid_coins:
        # coin is more or equal than the remaining cost
        if rem_cost <= coin:
            owed = coin - rem_cost
            print(f"Change Owed: {owed}")
            break
        # coin is less than the remaining cost
        else:
            rem_cost -= coin