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

# import random
# import string

# ALL_CHARS = string.digits + string.ascii_letters


# def generate_code(code_len=4):
#     """生成指定长度的验证码
    
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码字符串
#     """
#     return ''.join(random.choices(ALL_CHARS, k=code_len))

# for _ in range(10):
#     print(generate_code())

#!/usr/bin/python3

# def get_suffix(filename, ignore_dot=True):
#     """获取文件名的后缀名
    
#     :param filename: 文件名
#     :param ignore_dot: 是否忽略后缀名前面的点
#     :return: 文件的后缀名
#     """
#     # 从字符串中逆向查找.出现的位置
#     pos = filename.rfind('.')
#     # 通过切片操作从文件名中取出后缀名
#     if pos <= 0:
#         return ''
#     return filename[pos + 1:] if ignore_dot else filename[pos:]

# print(get_suffix('readme.txt'))       # txt
# print(get_suffix('readme.txt.md'))    # md
# print(get_suffix('.readme'))          #
# print(get_suffix('readme.'))          #
# print(get_suffix('readme'))           #

# from os.path import splitext

# def get_suffix(filename, ignore_dot=True):
#     return splitext(filename)[1][1:] if ignore_dot else splitext(filename)[1]

# print(get_suffix('readme.txt'))       # txt
# print(get_suffix('readme.txt.md'))    # md
# print(get_suffix('.readme'))          #
# print(get_suffix('readme.'))          #
# print(get_suffix('readme'))           #


# import math


# def ptp(data):
#     """求极差（全距）"""
#     return max(data) - min(data)


# def average(data):
#     """求均值"""
#     return sum(data) / len(data)


# def variance(data):
#     """求方差"""
#     x_bar = average(data)
#     temp = [(num - x_bar) ** 2 for num in data]
#     return sum(temp) / (len(temp) - 1)


# def standard_deviation(data):
#     """求标准差"""
#     return math.sqrt(variance(data))


# def median(data):
#     """找中位数"""
#     temp, size = sorted(data), len(data)
#     if size % 2 != 0:
#         return temp[size // 2]
#     else:
#         return average(temp[size // 2 - 1:size // 2 + 1])

        
# data = range(16)
# print(median(data))

# def isTriangle(a,b,c):
#     print(f'a={a},b={b},c={c}')
#     return a+b>c and b+c>0 and a+c >b

# print(isTriangle(3,4,1))


# Important
def calc(*args, **kwargs):
    result = sum(arg for arg in args if type(arg) in (int, float))
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10