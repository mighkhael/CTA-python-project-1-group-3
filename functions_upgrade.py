#for importing variables or functions from another file ------------> from functions import students_file   


import functions

# Function to add or update a student's grade for a course

def update_grade(name, course, grade):
    if name in functions.students_file:
        if course in functions.students_file[name]:
            functions.students_file[name][course] = grade
            print(f"Updated grade for {name} in {course} to {grade}.")
        else:
            print(f"Course '{course}' not found for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")
update_grade("Mike", "Maths", 78)
update_grade("Tega", "Maths", 98)
update_grade("Emeka", "Maths", 98)
update_grade("Sonia", "Maths", 20)



