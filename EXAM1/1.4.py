students = int(input())
grade5 = 0
grade4 = 0
grade3 = 0
grade_under3 = 0
average = 0

for i in range(students):
    grade = float(input())
    average += grade

    if grade >= 5:
        grade5 += 1
    elif 4.99 >= grade >= 4:
        grade4 += 1
    elif 3.99 >= grade >= 3:
        grade3 += 1
    elif grade < 3:
        grade_under3 += 1

grade5_percent = (grade5 / students) * 100
grade4_percent = (grade4 / students) * 100
grade3_percent = (grade3 / students) * 100
grade_under3_percent = (grade_under3 / students) * 100
average = average / students

print(f'Top students: {grade5_percent:.2f}%')
print(f'Between 4.00 and 4.99: {grade4_percent:.2f}%')
print(f'Between 3.00 and 3.99: {grade3_percent:.2f}%')
print(f'Fail: {grade_under3_percent:.2f}%')
print(f'Average: {average:.2f}')