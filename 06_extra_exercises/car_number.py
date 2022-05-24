start_number = int(input())
finish_number = int(input())

for number_1 in range(start_number, finish_number + 1):
    for number_2 in range(start_number, finish_number + 1):
        for number_3 in range(start_number, finish_number + 1):
            for number_4 in range(start_number, finish_number + 1):
                if number_1 % 2 == 0 and number_4 % 2 == 0:
                    continue
                if number_1 % 2 != 0 and number_4 % 2 != 0:
                    continue
                if number_1 <= number_4:
                    continue
                if (number_2 + number_3) % 2 != 0:
                    continue
                print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
