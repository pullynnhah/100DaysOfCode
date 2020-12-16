import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (student, score) in student_dict.items():
    print(f'Students: {student}')
    print(f'Scores: {score}')
print()

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

for (student, score) in student_data_frame.items():
    print(student)
    print(score)
print()

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print()

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    print()

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    
