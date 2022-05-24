needed_money = float(input())
current_money = float(input())
spending_counter = 0
days_counter = 0
spending_too_many_days = False
while current_money < needed_money:
    action = input()
    current_sum = float(input())
    days_counter += 1
    if action == "save":
        current_money += current_sum
        spending_counter = 0  # zeroing counter
    else:  # elif action == "spent"
        spending_counter += 1
        if spending_counter == 5:
            spending_too_many_days = True
            break
        current_money -= current_sum
        if current_money < 0:
            current_money = 0
if spending_too_many_days:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")
