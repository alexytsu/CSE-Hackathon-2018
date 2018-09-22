import csv
import re


with open("output.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("Coursename:", row[1])
        reqs = row[3]
        courses = re.findall("[A-Z]{4}[0-9]{4}", reqs)
        print("Prequisites", courses)