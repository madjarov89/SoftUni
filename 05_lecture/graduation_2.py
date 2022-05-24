name = input()

year = 1
total_mark = 0
counter = 0
while year <= 12:
    if counter > 1:
        break
    mark = float(input())
    if mark < 4:
        counter += 1
        continue
    total_mark += mark
    year += 1

if counter > 1:
    print(f"{name} has been excluded at {year} grade")
else:
    mean_mark = total_mark / 12  # /year
    print(f"{name} graduated. Average grade: {mean_mark:.2f}")
