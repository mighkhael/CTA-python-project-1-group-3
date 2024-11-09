def avg_grade(course):
    total_grade = 0
    course_count = 0

#iterates over the name and course to get the course count and sums up the total grade for each course
    for name, courses in students_file.items():
        if course in courses:
            course_count += 1
            total_grade += courses[course]
    avg_course = total_grade / course_count

        #prints the average of each course to 2 significant figure
    print(f"\nThe average grade for {course}: {avg_course:.2f}")

#updates average for each course
for course in ["Maths", "English", "Ecnomics", "Verbal"]:
    avg_grade(course) 
