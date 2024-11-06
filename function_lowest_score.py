#importing modules

import functions
import functions_upgrade

#function to get the lowest score in a particular course

def lowest_score(course):
	last_student = None
	lowest_grade = float("inf")
	for name, courses in functions.students_file.items():
		if course in courses and courses[course] <  lowest_grade: 
			lowest_grade = courses[course]
			last_student = name
	if last_student:
		return f"Lowest score in {course}: {last_student} with a score of  {lowest_grade}"
	else:
		return f"No scores found for the course: {course}"

#putting the function to use:

lowest = lowest_score("Maths")
print(lowest)