data = input()
total_money = 0
is_valid = True
while data != "NoMoreMoney":
    money = float(data)
    if money < 0:
        is_valid = False
        break
    total_money += money
    print(f"Increase: {money:.2f}")
    data = input()
if is_valid:
    print(f"Total: {total_money:.2f}")
else:
    print("Invalid operation!")
    print(f"Total: {total_money:.2f}")
