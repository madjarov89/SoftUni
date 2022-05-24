x = float(input())
y = float(input())
h = float(input())

front_wall = x * x
side_wall = x * y

roof_side = x * y
roof_front = x * h / 2
total_area_roof = 2 * roof_side + 2 * roof_front

total_area_front = 2 * (front_wall) - (1.2 * 2)
total_area_side = 2 * (side_wall) - (1.5 * 1.5 * 2)

wall_paint = (total_area_front + total_area_side) / 3.4
roof_paint = total_area_roof / 4.3


formated_wall_paint = "{:.2f}".format(wall_paint)
formated_roof_paint = "{:.2f}".format(roof_paint)


print(formated_wall_paint)
print(formated_roof_paint)