int_number = 10
float_number = 3.14
name = 'Dimitar'
data = input()
side_a = int(data)
# side_a = int(input())

print(int_number)
print(float_number)
print(name)

area = side_a * side_a
print(area)

first_name = input()
last_name = input()
age = int(input())

print(first_name + ' ' + last_name + ' @ ' + str(age))
print(f'{first_name} {last_name} @ {age}')

num_one = int(input())
num_two = int(input())

# Целочислено делени
result = num_one // num_two
print(result)  # 7 // 3 = 2

# Модулно деление
result1 = num_one % num_two
print(result1)  # 7 % 3 = 1

# Импортиране
import math

num = math.pi
print(num)
