# from datetime import date
# today = date(2015, 2, 20)
# print(today)
# freedom = date(2023, 2, 16)
# print(freedom)
# t = str(freedom - today)
# print(t)
# print(today.strftime('%A %B %d'))

# t = [1, 2, 3]
# t[1:3] = [t]
# t.extend(t)
# print(t)
# print(t[1][2])

t = [1]
t.append(t)

# [1,[1,[1,[1......]]]] 无线的内嵌
print(t)

# t = [[1, 2], [3, 4]]
# t[0].append(t[1:2])
# print(t)