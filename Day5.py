# """
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
# """
# for num in range(100, 1000):
#     low = num%10
#     mid = num//10%10
#     high = num//100
#     if num == low**3 + mid **3 + high **3:
#         print(num)

# for x in range(0,20):
#     for y in range(0, 33):
#         z = 100-x-y
#         if 5*x+3*y+z/3==100:
#             print('公鸡: %d, 母鸡：%d， 小鸡: %d' % (x, y, z))


from random import randint

money = 1000
while money > 0:
    print('you have:', money)
    needs_go_on = False
    while True:
        debt = int(input('debt: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('you got %d' % first)
    if first in [7, 11]:
        print('You win!')
        money += debt
    elif first in [2, 3, 12]:
        print('You lose!')
        money = money - debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('Yor got %d' % current)
        if current == 7:
            print('You lose')
            money = money - debt
        elif current == first:
            print('You win!')
            money = money + debt
        else:
            needs_go_on = True
print('You are poor!')


