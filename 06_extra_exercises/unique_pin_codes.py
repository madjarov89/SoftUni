first_number = int(input())
second_number = int(input())
third_number = int(input())

for number_1 in range(1, first_number + 1):
    if number_1 % 2 == 0:
        for number_2 in range(2, second_number + 1):
            if number_2 == 2 or number_2 == 3 or number_2 == 5 or number_2 == 7:
                for number_3 in range(1, third_number + 1):
                    if number_3 % 2 == 0:
                        print(number_1, number_2, number_3)


