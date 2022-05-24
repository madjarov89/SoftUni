degrees_celsius = float(input())
degrees_farenheit = degrees_celsius * 9/5 + 32

formated_degreees = "{:.2f}".format(degrees_farenheit)
print(formated_degreees)