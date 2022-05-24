skumria_price = float(input())
caca_price = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

midi_price = 7.50
palamud_price = skumria_price + skumria_price * 0.60
safrid_price = caca_price + caca_price * 0.8

total_palamud = palamud_price * kg_palamud
total_safrid = safrid_price * kg_safrid
total_midi = midi_price * kg_midi

total_price = total_palamud + total_safrid + total_midi
formated_price = "{:.2f}".format(total_price)

print(formated_price)
