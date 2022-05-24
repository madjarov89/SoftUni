days_of_stay = int(input())
room_type = input()
evaluation = input()
room_price = 0

if room_type == "room for one person":
    room_price = 18.00
elif room_type == "apartment":
    room_price = 25.00
    if days_of_stay < 10:
        room_price -= room_price * 0.30
    elif 10 <= days_of_stay <= 15:
        room_price -= room_price * 0.35
    else:
        room_price -= room_price * 0.50
elif room_type == "president apartment":
    room_price = 35.00
    if days_of_stay < 10:
        room_price -= room_price * 0.10
    elif 10 <= days_of_stay <= 15:
        room_price -= room_price * 0.15
    else:
        room_price -= room_price * 0.20

if evaluation == "positive":
    room_price += room_price * 0.25
else:
    room_price -= room_price * 0.10

total_price = room_price * (days_of_stay - 1)
print(f"{total_price:.2f}")
