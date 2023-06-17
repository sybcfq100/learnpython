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