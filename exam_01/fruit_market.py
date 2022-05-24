strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - raspberry_price * 0.40
banana_price = raspberry_price - raspberry_price * 0.80

needed_money = strawberry_quantity * strawberry_price + banana_quantity * banana_price + \
    orange_quantity * orange_price + raspberry_quantity * raspberry_price

print(f"{needed_money:.2f}")
