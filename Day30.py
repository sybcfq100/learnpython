from datetime import date
today = date(2015, 2, 20)
print(today)
freedom = date(2023, 2, 16)
print(freedom)
t = str(freedom - today)
print(t)
print(today.strftime('%A %B %d'))
