

import csv
import get_string


students = []

for i in range(3):
    name = get_string("name: ")
    dorm = get_string("dorm: ")
    students.append({"name": name, "dorm": dorm})

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    for student in students:
        writer.writerow((student["name"], student["dorm"]))
