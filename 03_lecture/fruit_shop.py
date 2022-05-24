fruit = input()
day = input()
amount = float(input())

is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" \
    or day == "Thursday" or day == "Friday"
is_weekend = day == "Sunday" or day == "Saturday"

price = 0
valid = True
if is_working_day:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        valid = False

elif is_weekend:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        valid = False
else:
    valid = False

if valid:
    final_price = price * amount
    print(f"{final_price:.2f}")
else:
    print("error")
