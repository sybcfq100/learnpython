# """
# 输入M和N计算C(M,N)

# Version: 0.1
# Author: 骆昊
# """
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m+1):
#     fm = fm * num
# fn = 1 
# for num in range(1, n+1):
#     fn = fn * num
# fm_n = 1
# for num in range(1, m-n+1):
#     fm_n = fm_n * num
# print(fm//fn//fm_n)

# def fac(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1, num + 1):
#         result = result * n
#     return result

# m = int(input('m = '))
# n = int(input('n = '))
# print(fac(m)//fac(n)//fac(m-n))

from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total = total + randint(1, 6)
    return total

def add(a = 0, b = 0, c = 0):
    return a + b + c

print(roll_dice())