number_of_days = int(input())
total_food_amount = float(input())

amount_biscuits = 0
total_food_amount_dog = 0
total_food_amount_cat = 0
days_counter = 0
eaten_food_amount = 0

for days in range(number_of_days):
    food_amount_dog = int(input())
    food_amount_cat = int(input())
    total_food_amount_dog += food_amount_dog
    total_food_amount_cat += food_amount_cat
    eaten_food_amount += food_amount_dog + food_amount_cat
    days_counter += 1
    if days_counter % 3 == 0:
        current_food_amount = food_amount_dog + food_amount_cat
        amount_biscuits += current_food_amount * 0.10

percent_eaten_food = eaten_food_amount / total_food_amount * 100
percent_dog = total_food_amount_dog / eaten_food_amount * 100
percent_cat = total_food_amount_cat / eaten_food_amount * 100

print(f"Total eaten biscuits: {round(amount_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")
