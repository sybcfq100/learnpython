# import itertools
# for x, y in itertools.product(range (20), range(33)):
#     z = 100-x-y
#     if 5*x + 3*y + z//3 == 100 and z % 3 ==0:
#         print(x, y ,z)

fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
