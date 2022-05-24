# Понеже Жоро предпочита да играе с приятели навън, вашата задача е
# да му помогнете да изчисли колко часа на ден трябва да отделя,
# за да прочете необходимата литература.

# От конзолата се четат 3 реда:
# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
# Ne e napisano, no trqbva da dava izhod cqlo chislo!

pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())
hours_for_book = pages / pages_per_hour
hours_per_day = int(hours_for_book / days_for_reading)
# hours_per_day = hours_for_book // days_for_reading

print(hours_per_day)
