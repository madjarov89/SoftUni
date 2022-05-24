sqr_m = float(input())
price = 7.61

total_price = sqr_m * price
discount = 0.18 * total_price
price_discount = total_price - discount

print(f'The final price is: {price_discount} lv.')
print(f'The discount is: {discount} lv.')
