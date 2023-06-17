# sum = 0
# for x in range(0,101,2):
#     sum = sum + x
# print(sum)

# sum = 0
# for x in range(101):
#     if x%2==0:
#         sum = sum + x
# print(sum)

# import random

# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter = counter + 1
#     number = int(input('please input number: '))
#     if number < answer:
#         print('try a larger number!')
#     elif number > answer:
#         print('try a smaller number!')
#     else:
#         print("you're right!")
#         break
# print('you take %d times' % counter)
# if counter > 7:
#     print('You lose!')

# """
# 输出乘法口诀表
# """
# for i in range(1,10):
#     for j in range(1,i+1):
#        print('%d * %d = %d' %(i, j, i*j), end = '\t')
#     print()
# """求两个数的最大公约数和最小公倍数·"""

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d and %d 的最大公约数是 %d' % (x, y, factor))
#         print('%d and %d 的最小公倍数是 %d' % (x, y, x * y // factor))
#         break

# row = int(input('inter number of row: '))
# for i in range(row):
#     for j in range(i+1):     # 如果在嵌套中用不到j，则可以用 _ 表示，作用是占位符
#         print('*', end='')
#     print()

# row = 5
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()