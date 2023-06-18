#  def make_adder(n):
#      ''' Return a function that takes one K and return K+N.
#      >>> add_three = make_adder(3)
#      >>> add_three(4)
#      7
#      '''
#      def adder(k):
#          return k + n
#
#      return adder
#
#
#  f = make_adder(2000)
#  print(f(13))
#  print(make_adder(1)(2))


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1



def is_three(x):
    return x == 3


print(search(is_three))
print(is_three(2))
#
#
# def square(x):
#     return x * x


#
#  def positive(x):
#      return max(0, square(x) - 100)
#
#
#  #  print(search(positive))
#
#
#  def inverse(f):
#      '''Return g(y) such that g(f(x)) --> x.'''
#      return lambda y: search(lambda x: f(x) == y)
#
# def sqrt(y):
#     def is_sqrt_of_y(x):
#         return square(x) == y

#     return search(is_sqrt_of_y)


# print(sqrt(36))
#
# sqrt = inverse(square)
# sqrt(256)
# def end(n, d):
#     while n > 0:
#         last, n = n % 10, n // 10
#         print(last)
#         if d == last:
#             # break
#             return None


# print(end(324567, 5))