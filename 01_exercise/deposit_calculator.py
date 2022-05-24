# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# От конзолата се четат 3 реда:
# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

# Да се отпечата на конзолата сумата в края на срока.

deposit = float(input())
months = int(input())
annual_interest_percent = float(input())
annual_interest = deposit * annual_interest_percent / 100
monthly_interest = annual_interest / 12

total_sum = deposit + months * monthly_interest

print(total_sum)
