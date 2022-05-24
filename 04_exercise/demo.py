n = int(input())

# Square
for row in range(1, n + 1):
    print('*', end='')
    for col in range(1, n):
        print(' *', end='')
    print()

# Rectangle
for row in range(0, n):
    for col in range(0, n):
        print('*', end='')
    print()

# Triangle
for row in range(n):
    print('*', end='')
    for col in range(row):
        print(' *', end='')
    print()

