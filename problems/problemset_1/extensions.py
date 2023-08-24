# implement a program that prompts the user for the name of a file
# and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes

file = input("File Name: ")
file = file.lower().strip()

if ".gif" in file:
    print("image/gif")
elif ".jpg" in file or ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
