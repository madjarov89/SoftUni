num = int(input())

sum_of_num = 0
max_number = ''
for i in range(num):
    current_number = int(input())
    if i == 0:
        max_number = current_number
    if current_number > max_number:
        max_number = current_number
    sum_of_num += current_number
if max_number == sum_of_num - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_of_num - max_number))
    print("No")
    print(f"Diff = {difference}")
