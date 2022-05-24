data = input()
total = 0
is_valid = True
while data != "NoMoreMoney":
    money = float(data)
    if money < 0:
        is_valid = False
        break
    total += money
    print(f"Increase: {money:.2f}")
    data = input()
if is_valid:
    print(f"Total: {total:.2f}")
else:
    print("Invalid operation!")
    print(f"Total: {total:.2f}")
