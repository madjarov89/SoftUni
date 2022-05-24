# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
#	Пилешко меню –  10.35 лв.
#	Меню с риба – 12.40 лв.
#	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

# От конзолата се четат 3 реда:
#	Брой пилешки менюта – цяло число в интервала [0 … 99]
#	Брой менюта с риба – цяло число в интервала [0 … 99]
#	Брой вегетариански менюта – цяло число в интервала [0 … 99]

# Да се отпечата на конзолата един ред:  "{цена на поръчката}"

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
needed_sum = chicken_menu * chicken_menu_count + \
    fish_menu * fish_menu_count + \
    vegan_menu * vegan_menu_count
desert_price = needed_sum * 0.20
delivery_price = 2.50

total_price = needed_sum + desert_price + delivery_price

print(total_price)
