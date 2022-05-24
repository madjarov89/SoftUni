width = int(input())
length = int(input())
total_cake_peaces = width * length
cake_is_over = False
command = input()
while command != "STOP":
    current_number_of_peaces = int(command)
    total_cake_peaces -= current_number_of_peaces
    if total_cake_peaces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(total_cake_peaces)} pieces more.")
else:
    print(f"{total_cake_peaces} pieces are left.")
