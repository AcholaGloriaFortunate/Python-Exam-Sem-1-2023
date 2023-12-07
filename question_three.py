self_age = int(input("Enter your age: "))

if self_age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")

#grades
def grade_students(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80 and mark <= 89:
        return "B"
    elif mark >= 70 and mark <= 79:
        return "C"
    elif mark >= 60 and mark <= 69:
        return "D"
    else:
        return "F"
    
student_mark = 85
result = grade_students(student_mark)
print(result)  

#modification
def grade_students(mark):
    if not isinstance(mark, int) and not isinstance(mark, float):
        return "Invalid input"

    if mark >= 90:
        return "A"
    elif mark >= 80 and mark <= 89:
        return "B"
    elif mark >= 70 and mark <= 79:
        return "C"
    elif mark >= 60 and mark <= 69:
        return "D"
    else:
        return "F"
valid_mark = 85
invalid_mark = "100"

score1 = grade_students(valid_mark)
score2 = grade_students(invalid_mark)

print(score1)  
print(score2)  


def grade_students(mark):
    if not isinstance(mark, int) and not isinstance(mark, float):
        return "Invalid input"

    if mark >= 90:
        return "A: Excellent"
    elif mark >= 80 and mark <= 89:
        return "B: Excellent"
    elif mark >= 70 and mark <= 79:
        return "C: Good"
    elif mark >= 60 and mark <= 69:
        return "D: Satisfactory"
    else:
        return "F: Needs Improvement"
student_mark1 = 90
student_mark2 = 83
student_mark3 = 71
student_mark4 = 60
student_mark5 = 30

score1 = grade_students(student_mark1)
score2 = grade_students(student_mark2)
score3 = grade_students(student_mark3)
score4 = grade_students(student_mark4)
score5 = grade_students(student_mark5)

print(score1)  
print(score2)  
print(score3)  
print(score4)  
print(score5)


def grade_students(mark):
    if not isinstance(mark, int) and not isinstance(mark, float):
        return "Invalid input", "Invalid input"

    if mark >= 90:
        return "A", "Excellent"
    elif mark >= 80 and mark <= 89:
        return "B", "Excellent"
    elif mark >= 70 and mark <= 79:
        return "C", "Good"
    elif mark >= 60 and mark <= 69:
        return "D", "Satisfactory"
    else:
        return "F", "Needs Improvement"
student_mark = 78
grade, correspondingmessage = grade_students(student_mark)

print(grade)   
print(correspondingmessage) 