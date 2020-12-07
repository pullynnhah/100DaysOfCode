# Don't change the code below
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Write your code below this row
count = 0
sum_ = 0
for student_height in student_heights:
    sum_ += student_height
    count += 1
avg_height = round(sum_ / count)

print(f'The average height is {avg_height}')
