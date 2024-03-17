"""
判断是不是素数
"""

from math import sqrt
num = int(input('please input a number:'))
end = int(sqrt(num))
is_prime = all(num % x != 0 for x in range(2, end + 1))
if is_prime and num != 1:
    print('%d 是素数' % num)
else:
    print('%d 不是素数' % num)

# def largest_factor(n):
#     for i in range(n - 1, 1, -1):
#         if n % i == 0:
#             print(i)
#             break
#     else:
#         print(1)

# largest_factor(79)

# def prime_factors(n):
#     while n > 1:
#         k = 2
#         while n % k != 0:
#             k += 1
#         n = n/k    # in the video teacher uses // i replace it by /, question is when it would be wrong?
#         print(k)

# prime_factors(78)


# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     return next(
#         (False for factor in range(2, int(sqrt(n)) + 1) if n % factor == 0),
#         n != 1,
#     )


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