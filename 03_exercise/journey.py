budget = float(input())
season = input()

budget_spent = 0
destination = ""
place = ""
if season == "summer":
    if budget <= 100:
        budget_spent = budget * 0.30
        destination = "Bulgaria"
        place = "Camp"
    elif budget <= 1000:
        budget_spent = budget * 0.40
        destination = "Balkans"
        place = "Camp"
    else:
        budget_spent = budget * 0.90
        destination = "Europe"
        place = "Hotel"

if season == "winter":

    if budget <= 100:
        budget_spent = budget * 0.70
        destination = "Bulgaria"
        place = "Hotel"
    elif budget <= 1000:
        budget_spent = budget * 0.80
        destination = "Balkans"
        place = "Hotel"
    else:
        budget_spent = budget * 0.90
        destination = "Europe"
        place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {budget_spent:.2f}")
