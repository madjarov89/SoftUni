budget = int(input())
season = input()
fishermen_count = int(input())

rent = 0
if season == "Spring":
    rent = 3000.00
    if fishermen_count <= 6:
        rent -= rent * 0.10
    elif 7 <= fishermen_count <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25
    if fishermen_count % 2 == 0:
        rent -= rent * 0.05

elif season == "Summer":
    rent = 4200.00
    if fishermen_count <= 6:
        rent -= rent * 0.10
    elif 7 <= fishermen_count <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25
    if fishermen_count % 2 == 0:
        rent -= rent * 0.05

elif season == "Autumn":
    rent = 4200.00
    if fishermen_count <= 6:
        rent -= rent * 0.10
    elif 7 <= fishermen_count <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25

elif season == "Winter":
    rent = 2600.00
    if fishermen_count <= 6:
        rent -= rent * 0.10
    elif 7 <= fishermen_count <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25
    if fishermen_count % 2 == 0:
        rent -= rent * 0.05

money_left = budget - rent
money_needed = rent - budget

if budget >= rent:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva.")
