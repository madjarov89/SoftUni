vacation_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3.0
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.0

total_price = puzzle_price * puzzle_count + talking_doll_price * talking_doll_count \
    + teddy_bear_price * teddy_bear_count + minion_price * minion_count \
    + truck_price * truck_count

total_count = puzzle_count + talking_doll_count + teddy_bear_count \
    + minion_count + truck_count

if total_count >= 50:
    total_price = total_price - total_price * 0.25

final_price = total_price - total_price * 0.10
left_over = final_price - vacation_price

if left_over >= 0:
    print(f"Yes! {left_over:.2f} lv left.")
else:
    left_over = abs(left_over)
    print(f"Not enough money! {left_over:.2f} lv needed.")

