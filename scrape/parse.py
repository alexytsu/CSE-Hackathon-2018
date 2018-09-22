import csv
import re


class Course():

    def __str__(self):
        return "<Course>: " +self._name

    def __repr__(self):
        return self.__str__()

    def __init__(self, name, reqs):
        self._name = name
        self._reqs = reqs
        self._tri1 = True
        self._tri2 = False
        self._tri3 = True


def get_all_prequisites(coursename):

    courselist = []

    with open("output.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            reqs = row[3]
            courses = re.findall("[A-Z]{4}[0-9]{4}", reqs)
            newCourse = Course(row[1], courses)
            courselist.append(newCourse)
        course = [x for x in courselist if x._name == coursename] 

    if(len(course) == 0):
        return []
    course = course[0]
    dependency_list = course._reqs
    print("Course: ", course._name, "Reqs: ", course._reqs)

    for x in course._reqs:
        dependency_list = dependency_list + get_all_prequisites(x)

    dependency_list = list(set(dependency_list))
    dependency_list = clean_list(dependency_list, courselist)
    dependency_list.sort()
    dependency_list = convert_names_to_courses(dependency_list)
    return dependency_list


def convert_names_to_courses(name_list):
    object_list = []

    courselist = []

    with open("output.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            reqs = row[3]
            courses = re.findall("[A-Z]{4}[0-9]{4}", reqs)
            newCourse = Course(row[1], courses)
            courselist.append(newCourse)
    

    for x in name_list:
        course = [obj for obj in courselist if x == obj._name]       
        assert len(course) == 1
        course = course[0]
        print("Course: ", course)
        object_list.append(course)
        
    return object_list


# removes courses that don't exist anymore
def clean_list(course_list, refcourselist):
    coursenames = [x._name for x in refcourselist]
    course_list = [x for x in course_list if x in coursenames]
    return course_list
