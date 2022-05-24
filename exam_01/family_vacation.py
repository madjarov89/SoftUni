budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_added_charges = int(input())

if number_of_nights > 7:
    price_per_night = price_per_night - price_per_night * 0.05

total_price = number_of_nights * price_per_night
added_charges = budget * percent_added_charges / 100

total_money_spent = total_price + added_charges
difference = abs(budget - total_money_spent)

if total_money_spent <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
