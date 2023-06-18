def bad_fabonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fabonacci(n-2) + bad_fabonacci(n-1)


def good_fabonacci(n):
    """ return pair of fibonacci numbers f(n) and f(n-1) """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fabonacci(n-1)
        return (a+b, a)
    

print(good_fabonacci(7))

# // fibonacci ?
# def fib(n):
#   a = 0
#   b = 1G
#   while b<n:
#     print (b)
#     temp = a
#     a = b
#     b = temp+b
# fib(10)
# 求前n项斐波那契额数
# num = int(input('number of term: '))
# a = 0
# b = 1
# for _ in range(num):
#     (a, b) = (b, a+b)
#     print(a, end='\n')