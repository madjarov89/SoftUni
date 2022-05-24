movie_type = input()
rows = int(input())
cols = int(input())

cinema_seats = rows * cols
income = 0

if movie_type == "Premiere":
    income = cinema_seats * 12.00
elif movie_type == "Normal":
    income = cinema_seats * 7.50
elif movie_type == "Discount":
    income = cinema_seats * 5.00

print(f"{income:.2f} leva")
