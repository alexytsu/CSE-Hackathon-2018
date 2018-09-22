import csv
import re

from course import Course

courses = []

with open("output.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        reqs = row[3]
        courses = re.findall("[A-Z]{4}[0-9]{4}", reqs)
        courses.append[Course(row[1], reqs)]

for course in courses:
    print("---------------------------------------------")
    print("Course: ", course._name)
    print("Requisites: ", course._reqs)




    
