import math

figure = input()

area = 0
if figure == "square":
    side = float(input())
    area = side * side
#    print(f"{area:3f}")

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
#    print(f"{area:3f}")

elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
#    print(f"{area:3f}")

elif figure == "triangle":
    side = float(input())
    h = float(input())
    area = side * h / 2
#    print(f"{area:3f}")
print(f"{area:3f}")

