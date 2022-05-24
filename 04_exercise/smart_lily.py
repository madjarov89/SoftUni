age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
money_present = 0
toy_present = 0
money_from_toys = 0

for number in range(1, age+1):
    if number % 2 == 1:
        toy_present += 1
    else:
        money_present += 10
        total_money += money_present - 1

money_from_toys = toy_present * toy_price
final_money = total_money + money_from_toys
difference = abs(final_money - washing_machine_price)

if final_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
