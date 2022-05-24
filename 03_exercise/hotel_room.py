month = input()
nights_stay = int(input())
apartment = 0
studio = 0

if month == "May" or month == "October":
    apartment = 65
    studio = 50
    if nights_stay > 14:
        studio -= studio * 0.30
    elif nights_stay > 7:
        studio -= studio * 0.05
elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    if nights_stay > 14:
        studio -= studio * 0.20
elif month == "July" or month == "August":
    apartment = 77
    studio = 76

if nights_stay > 14:
    apartment -= apartment * 0.10

apartment_price = nights_stay * apartment
studio_price = nights_stay * studio

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
