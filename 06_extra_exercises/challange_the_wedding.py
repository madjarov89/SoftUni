male_clients = int(input())
female_clients = int(input())
number_of_tables = int(input())

occupied_tables = 0
for man in range(1, male_clients + 1):
    for woman in range(1, female_clients + 1):
        occupied_tables += 1
        print(f"({man} <-> {woman})", end=" ")
        if occupied_tables == number_of_tables:
            break
    if occupied_tables == number_of_tables:
        break
