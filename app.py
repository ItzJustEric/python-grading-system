

student_grades = {
    "eric":92,
    "Mike":75,
    "Jayson":96,
    "Leah":82,
    "Andrea":55

}
failing_students = []
passing_students = []

for x in student_grades:
    if student_grades[x] < 60:
        failing_students.append(x)
    elif student_grades[x] >= 60:
        passing_students.append(x)



subjects = ("math","english","science","spanish","computerScience","music","art")

start_system = input("Welcome back would you like to add new data or edit existing data into the system(E/N): ")
choose_classes = input("What class is this for: ")

if choose_classes  in subjects:


    if start_system == "E":
        student_name = input("enter the name of the student: ")
        if student_name in student_grades:
            student_grade_update = input("enter the new grade: ")
            current_grade = student_grades[student_name]
            updated_grade = int(student_grade_update)
            print(student_name + f" new grade in {choose_classes} is {str(updated_grade)}")
            student_grades.update({student_name: updated_grade})
            print(student_grades)
        elif student_name not in student_grades:
            print("please enter an existing student name")

        if updated_grade < 60:
            failing_students.append(student_name)
        elif updated_grade >= 60:
            if current_grade < 60:
                failing_students.remove(student_name)
                passing_students.append(student_name)











    elif start_system == "N":
        new_student = input("enter the name of the new student: ")
        new_student_grade = int(input("enter the grade for the new student: "))
        student_grades.update({new_student: new_student_grade})
        print(f"we added {new_student} to the system and they have a {new_student_grade} in {choose_classes}")
        print(student_grades)

        if new_student_grade < 60:
            failing_students.append(new_student)
        elif new_student_grade >= 60:
            passing_students.append(new_student)





    else:
        print("please enter a valid class")


print(f"here is a list of passing students :  {', '.join(passing_students)}")
print(f"here is  a list of failing students : {', '.join(failing_students)}")









