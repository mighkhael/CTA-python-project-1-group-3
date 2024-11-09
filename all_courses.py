#importing modules

import functions
import functions_upgrade
import  average_grades 


#Function to display all students and their grades

def display_all_student_grades():
    for name, courses in functions.students_file.items():
        grades = ",   ".join([f"{course}: {grade}" for course, grade in courses.items()])
        print(f"{name}'s grades = {grades}")

display_all_student_grades() 
