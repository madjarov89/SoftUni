from math import pi

r = float(input())
area = pi * r ** 2
perimeter = 2 * pi * r

formated_area = "{:.2f}".format(area)
formated_perimeter = "{:.2f}".format(perimeter)


print(formated_area)
print(formated_perimeter)

