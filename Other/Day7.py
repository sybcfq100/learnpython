# import os
# import time

# def main():
#     content = '北京欢迎您，为您开天辟地......'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:]+content[0]


# if __name__ == '__main__':
#     main()

# numbers1 = [35, 12, 8, 99, 60, 52]
# numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
# print(numbers2)    # [144, 64, 3600, 2704]

import matplotlib.pyplot as plt

f = []


def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr


for i in range(1, 30):
    y = fib(i)
    f.append(y)
fig, ax = plt.subplots()
plt.plot(f, "bo-")
plt.show()

# list1 = [1,3,5,7,100]
# for index in range(len(list1)):
#     print(list1[index])

# for elem in list1:
#     print(elem)

# for index, elem in enumerate(list1):
#     print(index, '\t', elem)

# list1.append(200)
# print(list1)
# list1.insert(2, 400)
# print(list1)
# print(len(list1))
# if 1234 in list1:
#     list1.remove(3)
# print(list1)
# list1.pop(0)
# print(list1)

# import sys
# f = (x**2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)
