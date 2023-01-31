#  def apply_twice(f, x):
#      return f(f(x))
#
#  def f_square(x):
#      return x * x
#
#  print(apply_twice(f_square, 10))

# def repeat(f, x):
#     while f(x) != x:
#         x = f(x)
#     return x

# def g(y):
#     return (y + 5) // 3


# print(repeat(g, 5))

#  def make_adder(n):
#      def adder(k):
#          return k + n
#      return adder
#
#  def square(x):
#      return x * x
#
#  def triple(x):
#      return 3 * x
#
#  def compose1(f, g):
#      def h(x):
#          return f(g(x))
#      return h
#
#  print(compose1(triple, square)(5))

#  def print_sums(x):
    #  print(x)
    #  def next_sum(y):
    #      return print_sums(x+y)
    #  return next_sum
    #
#  print_sums(3)(4)(5)(6)

#  def f(x):
#      me = 1
#      def g(y):
#          return me
#      me = 2
#      print(g(7))
#      return x + y
#
#
#  y = 1
#  z = f(2)

#  def curry2(f):
#      def g(x):
#          def h(y):
#              return f(x, y)
#          return h
#      return g
#  # curried_pow = curry2(pow)
#  # two_to_the = curried_pow(2)
#
#  # x = two_to_the(5)
#  x = curry2(pow)(2)(5)
#  print(x)

# def square(x):
#     return x * x

# def make_adder(n):
#     def adder(k):
#         return n + k
#     return adder

# def compose1(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# print(compose1(square, make_adder(2))(3))

# higher_order_lambda = lambda f: lambda x: f(x)

# g = lambda x: x * x
# print(higher_order_lambda(g)(2))

def coffee(grounds):
    x = 4
    return grounds(x)
x = 6
print(coffee(lambda x: x + 10))