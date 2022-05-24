destination = input()

while destination != "End":
    trip_price = float(input())

    sum_current_destination = 0
    while sum_current_destination < trip_price:
        saved_money = float(input())
        sum_current_destination += saved_money

    print(f"Going to {destination}!")

    destination = input()
