# Booleans
a = 5
b = 10
print(a > 5)
print(a == b)
print(b > a)
print(b <= 10)

a = input()
b = input()
print(a == b)

a = int(input())
is_positive = (a > 0)
print(is_positive)

# Rounding
import math

up = math.ceil(23.45)
down = math.floor(45.67)
absolute = abs(-50)
round_number = round(45.67852, 2)
print(up, down, absolute, round_number)

# Format
print(f"{123.456:.2f}")
