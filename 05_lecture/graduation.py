name = input()
mark = float(input())

grade = 1
counter = 0
student_in_school = True
total_mark = 0

while student_in_school:
    if mark >= 4.00:
        total_mark += mark
        grade += 1
        mark = float(input())
        if grade == 12:
            total_mark += mark
            student_in_school = False
    else:
        counter += 1
        if counter >= 2:
            student_in_school = False
            mark = float(input())

mean_mark = total_mark / grade

if counter < 2:
    print(f"{name} graduated. Average grade: {mean_mark:.2f}")
else:
    print(f"{name} has been excluded at {grade} grade")
