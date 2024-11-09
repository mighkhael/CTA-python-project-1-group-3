import random



def update_grade(name, courses):
    if name in students_file:
        for course in courses:
            students_file[name][course] = random.randint(1, 100)
        print(f"\nUpdated grades for '{name}': ")
        for course, grade in students_file[name].items():
            print(f"{course}: {grade}")
            
for student in ["Mike", "Angela", "Daniel"]:
    update_grade(student, ["Maths", "English", "Ecnomics", "Verbal"])
