tab = int(input())
salary = float(input())

fee = 0
for site in range(tab):
    website = input()
    if website == "Facebook":
        fee += 150
    if website == "Instagram":
        fee += 100
    if website == "Reddit":
        fee += 50
    if fee >= salary:
        print("You have lost your salary.")
        break

difference = salary - fee
if fee < salary:
    print(round(difference))
