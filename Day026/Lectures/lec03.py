from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {student: randint(0, 100) for student in names}
print(student_score)

passed_students = {student: score for (student, score) in student_score.items() if score >= 60}
print(passed_students)
