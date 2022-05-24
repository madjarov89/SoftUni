budget = float(input())
destination = input()
season = input()
days_count = int(input())

price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    elif destination == "London":
        price_per_day = 24000

if season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    elif destination == "London":
        price_per_day = 20250

total_price = price_per_day * days_count

final_price = 0
if destination == "Dubai":
    final_price = total_price - total_price * 0.30
elif destination == "Sofia":
    final_price = total_price + total_price * 0.25
else:
    final_price = total_price

difference = abs(budget - final_price)

if budget >= final_price:
    print(f"The budget for the movie is enough! We have {difference} leva left!")
else:
    print(f"The director needs {difference} leva more!")
