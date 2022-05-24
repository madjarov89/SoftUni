import math

hours = int(input())
minutes = int(input())

# minutes += 15
# minutes %= 60
# hour += minutes // 60
# if hour > 23:
#    hour = 0

sum_minutes = minutes + 15
total_minutes = sum_minutes % 60
sum_hours = math.floor(hours + sum_minutes // 60)

total_hours = 0
if sum_hours > 23:
    total_hours = sum_hours % 24
else:
    total_hours = sum_hours

if total_minutes < 10:
    print(f"{total_hours}:0{total_minutes}")
else:
    print(f"{total_hours}:{total_minutes}")
