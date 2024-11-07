#importing modules

import functions
import functions_upgrade
import  average_grades 

# Function to display all course averages

def display_course_averages():

    unique_courses = set()   # set to store the courses


#here all unique courses are collected from student_file
    for student, courses in functions.students_file.items():
        unique_courses.update(courses.keys())

# cal and display the averages for each course
    for course in unique_courses:
        avg = average_grades.course_average(course)
        if isinstance(avg, float):
            print(f"Average grade for {course}:  {avg: .2f}") 
        else:
            print(f"The course: {course} has no registered grade")       

display_course_averages()



#Function to display all students and their grades

def display_all_student_grades():
    for name, courses in functions.students_file.items():
        grades = ",   ".join([f"{course}: {grade}" for course, grade in courses.items()])
        print(f"{name}'s grades = {grades}")

display_all_student_grades() 


