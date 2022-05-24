number = int(input())

# is_range = number >= 100 and number <= 200
# is_zero = number == 0
# valid = is_range or is_zero

valid = (number >= 100 and number <= 200) or number == 0

if not valid:
    print("invalid")

