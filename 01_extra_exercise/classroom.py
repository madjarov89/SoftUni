from math import floor

w = float(input())
h = float(input())

w_cm = h * 100
h_cm = w * 100

col = floor(h_cm / 120)
row = floor((w_cm - 100) / 70)
total_spaces = (col * row) - 3

print(total_spaces)
