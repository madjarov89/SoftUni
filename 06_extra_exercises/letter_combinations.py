letter_1 = input()
letter_2 = input()
letter_3 = input()

char_1 = ord(letter_1)
char_2 = ord(letter_2)
char_3 = ord(letter_3)

counter = 0
for symbol_1 in range(char_1, char_2 + 1):
    for symbol_2 in range(char_1, char_2 + 1):
        for symbol_3 in range(char_1, char_2 + 1):
            if symbol_1 == char_3 or symbol_2 == char_3 or symbol_3 == char_3:
                continue
            counter += 1
            transformed_symbol_1 = chr(symbol_1)
            transformed_symbol_2 = chr(symbol_2)
            transformed_symbol_3 = chr(symbol_3)
            print(f"{transformed_symbol_1}{transformed_symbol_2}{transformed_symbol_3}", end=" ")
print(counter)
