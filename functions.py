# functions definitions

students_file = {}   #A dictionary that holds student's subjects and initial grades

# Function to register a student and initialize their courses with a grade of 0
def register_student(name, courses):
    if isinstance(courses, str):				    # Ensure `courses` is a list, even if a single course is passed
        courses = [courses]
    
    newly_registered_courses = []            
    already_registered_courses = []			# Track newly registered and already registered courses for output
    
    if name in students_file:                          # Student already exists, add only new courses
        for course in courses:
            if course not in students_file[name]:  # Check if course is new
                students_file[name][course] = 0      # Initialize new course with a grade of 0
                newly_registered_courses.append(course)
            else:                                                                # Track courses that were already registered
                already_registered_courses.append(course)         
        all_courses_with_grades = " ".join([f"{course}: {grade}" for course, grade in students_file[name].items()])
        
        if newly_registered_courses:
            print(f"Updated courses for '{name}' with initial grades: {all_courses_with_grades}.")
        if already_registered_courses:
            print(f"Student '{name}' is already registered in courses: {" ".join(already_registered_courses)}.")
            
    else:											# Register new student with all courses and initial grades
        students_file[name] = {course: 0 for course in courses}
        all_courses_with_grades = ', '.join([f"{course}: 0" for course in courses])
        print(f"Student '{name}' registered successfully with courses and initial grades: {all_courses_with_grades}.")

#calling the function with different courses.
register_student("Mike", ["Maths", "English", "Ecnomics"])
register_student("Mike", ["Maths", "English", "Ecnomics", "Verbal"])



