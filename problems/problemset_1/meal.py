# implement a program that prompts the user for a time
# and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. 
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# convert is a function (that can be called by main) that converts time, 
# a str in 24-hour format, to the corresponding number of hours as a float. 
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.


def main():
    time_input = input("Give time input: ")

    if (convert(time_input) >= 7.0 and convert(time_input) <= 8.0):
        print("breakfast time")
    elif (convert(time_input) >= 12.0 and convert(time_input) <= 13.0):
        print("lunch time")
    elif (convert(time_input) >= 18.0 and convert(time_input) <= 19.0):
        print("dinner time")

    
def convert(time):
    hour, minutes = time.split(":")

    hour = int(hour)
    minutes = float(minutes)

    decimal = minutes / 60
    new_time = hour + decimal

    return new_time


if __name__ == "__main__":
    main()