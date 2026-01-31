# accepts students name age and course, return a single formatted string, dont print anything

def student_formatter(student_name, student_age, student_course):
    return f"{student_name} who is {student_age} is doing {student_course}"

student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
student_course = input("Enter student's course: ")
print(student_formatter(student_name, student_age, student_course))