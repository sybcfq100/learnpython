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

# from random import randint

# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total = total + randint(1, 6)
#     return total

# def add(a = 0, b = 0, c = 0):
#     return a + b + c

# print(roll_dice())

# import random

# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0
# for _ in range(6):
#     face = random.randint(1,6)
#     if face == 1:
#         f1 += 1
#     elif face == 2:
#         f2 += 1
#     elif face == 3:
#         f3 += 1
#     elif face == 4:
#         f4 += 1
#     elif face == 5:
#         f5 += 1
#     else:
#         f6 += 1
# print(f'1 点出现了{f1}次')
# print(f'2 点出现了{f2}次')
# print(f'3 点出现了{f3}次')
# print(f'4 点出现了{f4}次')
# print(f'5 点出现了{f5}次')
# print(f'6 点出现了{f6}次')

# 用字典生成式语法创建字典
# items = {x: x**3 for x in range(6)}
# print(items)
# 
# sentence = input('请输入一段话: ')
# counter = {}
# for _ in sentence:
    # if 'A' <= _ <= 'Z' or 'a' <= _ <= 'z':
        # counter[_] = counter.get(_, 0) + 1
# for key, value in counter.items():
    # print(f'字母{key}出现了{value}次.')

import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    """生成指定长度的验证码
    
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(10):
    print(generate_code())