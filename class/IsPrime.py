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