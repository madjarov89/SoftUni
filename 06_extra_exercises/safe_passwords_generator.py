number_a = int(input())
number_b = int(input())
max_passwords_amount = int(input())

current_password_amount = 0
stop = False
for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, number_a + 1):
            for y in range(1, number_b + 1):
                current_password_amount += 1
                if current_password_amount > max_passwords_amount:
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64
                if x == number_a and y == number_b:
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
    if stop:
        break
