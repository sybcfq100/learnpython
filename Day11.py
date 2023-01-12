# def main():
#     f = None
#     try:
#         f = open('0.05rpc.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('cannot open the file!')
#     except LookupError:
#         print('unknown coding error')
#     finally:
#         if f:
#             f.close()

# if __name__ == '__main__':
#     main()

# import time

# def main():
    # 一次性读取整个文件内容
#     with open('0.05rpc.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
# # 通过for-in循环逐行读取
#     with open('0.05rpc.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print() 
   # 读取文件按行读取到列表中
#     with open('0.05rpc.txt') as f:
#         lines = f.readlines()
#     print(lines)
       
        
    
# if __name__ == '__main__':
#     main()


# from math import sqrt
'''
计算最大公约数和最小公倍数
'''

x = int(input('x = '))
y = int(input('y = '))
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x*y//factor}')
        break
# '''
# 输入一个数，判断是不是素数
# '''


# num = int(input('inter a number: '))
# end = int(num**0.5)
# isPrime = True
# for x in range(2, end):
#     if num%x == 0:
#         isPrime = False
#         break
# if isPrime and num != 1:
#     print(f'{num} is prime!')
# else:   
#     print(f'{num} is not prime!')


# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     return next(
#         (False for factor in range(2, int(sqrt(n)) + 1) if n % factor == 0),
#         n != 1,
#     )


# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         fs_list.extend(open(filename, 'w', encoding='utf-8') for filename in filenames)
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误!')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成!')


# if __name__ == '__main__':
#     main()


# shakes = open('shakespeare.txt')
# text = shakes.read().split()
# len(text)