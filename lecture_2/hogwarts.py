# LISTS
# students = ["Sirius", "James", "Remus"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# DICTIONAIRIES
students = [
    {"name": "Remus", "last_name": "Lupin", "house": "Gryffindor"},
    {"name": "James", "last_name": "Potter", "house": "Gryffindor"},
    {"name": "Petunia", "last_name": "Evans", "house": None}
]

for student in students:
    print(student["name"])