# Напишете програма, която изчислява колко пари ще трябва да събере Ани,
# за да плати сметката, като имате предвид следния ценоразпис:
#	Пакет химикали - 5.80 лв.
#	Пакет маркери - 7.20 лв.
#	Препарат - 1.20 лв (за литър).

# От конзолата се четат 4 числа:
#	Брой пакети химикали - цяло число в интервала [0...100]
#	Брой пакети маркери - цяло число в интервала [0...100]
#	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#	Процент намаление - цяло число в интервала [0...100]

# Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.

number_of_pens = int(input())
number_of_markers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
price_per_liter_detergent = 1.20

total_sum = number_of_pens * price_per_pen \
             + number_of_markers * price_per_marker \
             + liters_of_detergent * price_per_liter_detergent

total_sum -= total_sum * percent_discount / 100

print(total_sum)
