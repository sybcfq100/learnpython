# def sum_squares(a, b):
#     return square(a) + square(b)

# def f(x):
#     return x * x

# square = f
# y = sum_squares(2, 3)
# print(y)

# def view(re):
#     # ice = 4
#     def k(means):
#         return re(means)
#     return k

# def review(pr):
#     return re(pr * 2)

# ice = 3
# re = view(lambda pr: pr * ice)
# print(review(1))

# def flip(flop):
#     if flop > 2:
#         return None
#     flip = lambda flip: 3
#     # return None if flop > 2 else (lambda flip: 3)

# def flop(flip):
#     return flop

# flip, flop = flop, flip

# print(flip(flop(1)(2))(3))

# def remove(n, digit):
#     '''
#     >>> remove(231, 3)
#     21
#     >>> remove(243132, 2)
#     4313
#     '''
#     kept, digits = 0 , 0
#     while n > 0:
#         n, last = n //10, n % 10
#         if last != digit:
#             kept = kept +  last * 10 ** digits
#             digits += 1
#     return kept

# print(remove(243132, 2))

# def trace1(fn):
#     def traced(x):
#         print('Calling', fn, 'on argument', x)
#         return fn(x)
#     return traced

# @trace1
# def square(x):
#     return x * x

# @trace1
# def sum_squares_up_to(n):
#     k = 1
#     total = 0
#     while k <= n:
#         total, k = total + square(k), k + 1
#     return total

# print(sum_squares_up_to(5))

def repeat(k):
    '''
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    '''
    return detector(lambda j: False)(k)

def detector(have_seen):
    def g(i):
        if have_seen(i):
            print(i)
        new_have_seen = lambda j: j == i or have_seen(j)
        return detector(new_have_seen)
        # return detector(lambda j: j == i or have_seen(j))
    return g

repeat(1)(7)(7)
