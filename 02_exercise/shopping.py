budget = float(input())
n = int(input())
m = int(input())
p = int(input())
n_price = 250
n_money = n * n_price

m_price = n_money * 0.35
m_money = m * m_price

p_price = n_money * 0.10
p_money = p * p_price

total_money = n_money + m_money + p_money
if n > m:
    total_money = total_money - total_money * 0.15
if total_money <= budget:
    left_over = budget - total_money
    print(f"You have {left_over:.2f} leva left!")
else:
    needed_sum = total_money - budget
    print(f"Not enough money! You need {needed_sum:.2f} leva more!")
