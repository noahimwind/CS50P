# implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

grocery_dict = {}

def main():
    grocery_list()

def grocery_list():
    while True:
        try:
            chosen_item = input().upper()
            if chosen_item in grocery_dict:
                grocery_dict[chosen_item] += 1
            else:
                grocery_dict[chosen_item] = 1
        except EOFError:
            for key in sorted(grocery_dict.keys()):
                print(grocery_dict[key], key)
            break

main()