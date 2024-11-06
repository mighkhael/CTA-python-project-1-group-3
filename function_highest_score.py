#importing modules

import functions
import functions_upgrade

# Function to get the highest score in a particular subject

def highest_score(course):
    max_score = -1
    top_student =  None    #functions.students_file[name]
    for name, courses in functions.students_file.items():
        if course in courses and courses[course] > max_score:
            max_score = courses[course]
            top_student = name
    if top_student:
        return f"Highest score in {course}:  {top_student} with a score of {max_score}"
    else:
        return f"No scores found for the course '{course}'."

#to use the function 

highest_grade = highest_score("Maths")
print(highest_grade)
