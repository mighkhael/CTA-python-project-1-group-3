#importing modules: 

import functions
import functions_upgrade
from statistics import mean 

# function to calculate and return course averages

def course_average(course_name):
    
    course_grades = []                                 #Place all grades for each course into a list so average grade will be cal.

    for name, courses in functions.students_file.items():
        if course_name in courses:
            course_grades.append(courses[course_name])
    
    # Calculate and return course averages from course_grades, otherwise return None

    return mean(course_grades) if  course_grades else "Zero (0), no course has been registered yet"

maths = course_average("Maths")
print(f"The average grade for this course is : {maths}")



