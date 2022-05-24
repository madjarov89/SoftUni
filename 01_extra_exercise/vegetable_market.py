price_vegetables_lv = float(input())
price_fruis_lv = float(input())
amount_vegetables = int(input())
amount_fruits = int(input())

price_vegetables_eur = price_vegetables_lv / 1.94
price_fruis_eur = price_fruis_lv / 1.94

total_price_vegetables = price_vegetables_eur * amount_vegetables
total_price_fruits = price_fruis_eur * amount_fruits

total_money = total_price_vegetables + total_price_fruits
formated_money = "{:.2f}".format(total_money)

print(formated_money)
