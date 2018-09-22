import csv
import re

from course import Course

courselist = []

with open("output.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        reqs = row[3]
        courses = re.findall("[A-Z]{4}[0-9]{4}", reqs)
        newCourse = Course(row[1], courses)
        courselist.append(newCourse)


def get_all_prequisites(coursename):

    course = [x for x in courselist if x._name == coursename] 
    if(len(course) == 0):
        return []
    course = course[0]
    dependency_list = course._reqs
    print("Course: ", course._name, "Reqs: ", course._reqs)

    for x in course._reqs:
        dependency_list = dependency_list + get_all_prequisites(x)

    return dependency_list
    

# removes courses that don't exist anymore
def clean_list(course_list):
    coursenames = [x._name for x in courselist] 
    course_list = [x for x in course_list if x in coursenames]
    return course_list
    

courses2do = list(set(get_all_prequisites('COMP3421')))
print("courses2do", courses2do)
print(clean_list(courses2do))