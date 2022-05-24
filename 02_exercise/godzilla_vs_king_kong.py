budget_money = float(input())
statists_count = int(input())
clothes_price = float(input())

decor_price = budget_money * 0.1

if statists_count > 150:
    clothes_price = clothes_price - clothes_price * 0.1
    # clothes_price *= 0.9

total_clothes_price = statists_count * clothes_price
needed_money = total_clothes_price + decor_price

if needed_money > budget_money:
    missing_money = needed_money - budget_money
    print("Not enough money!")
    print(f"Wingard needs {missing_money:.2f} leva more.")
else:
    left_over = budget_money - needed_money
    print("Action!")
    print(f"Wingard starts filming with {left_over:.2f} leva left.")
