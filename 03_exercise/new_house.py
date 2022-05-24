flower_type = input()
flower_count = int(input())
budget = int(input())

rose_price = 5.00
dahlia_price = 3.80
tulip_price = 2.80
narcis_price = 3.00
gladiola_price = 2.50

flowers_price = 0
if flower_type == "Roses":
    if flower_count > 80:
        flowers_price = rose_price - rose_price * 0.10
    else:
        flowers_price = rose_price

elif flower_type == "Dahlias":
    if flower_count > 90:
        flowers_price = dahlia_price - dahlia_price * 0.15
    else:
        flowers_price = dahlia_price

if flower_type == "Tulips":
    if flower_count > 80:
        flowers_price = tulip_price - tulip_price * 0.15
    else:
        flowers_price = tulip_price

if flower_type == "Narcissus":
    if flower_count < 120:
        flowers_price = narcis_price + narcis_price * 0.15
    else:
        flowers_price = narcis_price

if flower_type == "Gladiolus":
    if flower_count < 80:
        flowers_price = gladiola_price + gladiola_price * 0.20
    else:
        flowers_price = gladiola_price

price = flowers_price * flower_count
money = abs(budget - price)


if price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {money:.2f} leva more.")
