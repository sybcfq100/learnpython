# from operator import add, mul


# def square(x):
#     return x * x


# def identity(x):
#     return x


# def triple(x):
#     return 3 * x


# def increment(x):
#     return x + 1


#  def ordered_digits(x):
#  """Return True if the (base 10) digits of X>0 are in non-decreasing
#  order, and False otherwise.
#
#  >>> ordered_digits(5)
#  True
#  >>> ordered_digits(11)
#  True
#  >>> ordered_digits(127)
#  True
#  >>> ordered_digits(1357)
#  True
#  >>> ordered_digits(21)
#  False
#  >>> result = ordered_digits(1375) # Return, don't print
#  >>> result
#  False
#
#  """
#  "*** YOUR CODE HERE ***"
#  for _ in range(len(str(x))):
#      rest, last = x // 10, x % 10
#      if rest % 10 > last:
#          return False
#      return True
# alternative solution
#      last = x % 10
#  x = x // 10
#  while x > 0 and last >= x % 10:
#      last = x % 10
#      x = x // 10
#  return x == 0
#  print(ordered_digits(13579))

# def get_k_run_starter(n, k):
#     """Returns the 0th digit of the kth increasing run within n.
#     >>> get_k_run_starter(123444345, 0) # example from description
#     3
#     >>> get_k_run_starter(123444345, 1)
#     4
#     >>> get_k_run_starter(123444345, 2)
#     4
#     >>> get_k_run_starter(123444345, 3)
#     1
#     >>> get_k_run_starter(123412341234, 1)
#     1
#     >>> get_k_run_starter(1234234534564567, 0)
#     4
#     >>> get_k_run_starter(1234234534564567, 2)
#     2
#     """
#     i = 0
#     final = None
#     while i <= k:
#         while n > 10 and (n % 10) > (n // 10) % 10:
#             n = n // 10
#         final = n % 10
#         i = i + 1
#         n = n // 10
#     return final

# print(get_k_run_starter(123444345, 1))

#  def make_repeater(func, n):
#      """Return the function that computes the nth application of func.
#
#      >>> add_three = make_repeater(increment, 3)
#      >>> add_three(5)
#      8
#      >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
#      243
#      >>> make_repeater(square, 2)(5) # square(square(5))
#      625
#      >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
#      152587890625
#      >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
#      5
#      """
#      "*** YOUR CODE HERE ***"
#
#      # g = identity
#      # while n > 0:
#      #     g = composer(func, g)
#      #     n = n - 1
#      # return g
#      # Alternative solutions
#      def inner_func(x):
#          k = 0
#          while k < n:
#              x, k = func(x), k + 1
#          return x
#
#      return inner_func
#
#
#  def composer(func1, func2):
#      def f(x):
#          return func1(func2(x))
#      return f
#
#
#  print(make_repeater(triple, 5)(1))

# def composer(func1, func2):
#     """Return a function f, such that f(x) = func1(func2(x))."""

#     def f(x):
#         return func1(func2(x))

#     return f

#  def apply_twice(func):
#  """ Return a function that applies func twice.
#
#  func -- a function that takes one argument
#
#  >>> apply_twice(square)(2)
#  16
#  """
#  "*** YOUR CODE HERE ***"
#  def f(x):
#      return func(x)**2
#  return f
#
#
#  print(apply_twice(square)(2))

# def div_by_primes_under(n):
#    """
#    >>> div_by_primes_under(10)(11)
#    False
#    >>> div_by_primes_under(10)(121)
#    False
#    >>> div_by_primes_under(10)(12)
#    True
#    >>> div_by_primes_under(5)(1)
#    False
#    """
#    checker = lambda x: False
#    i = 2
#    while i <= n:
#       if not checker(i):
#         #    checker = lambda x: True if x % i == 0 else False
#           checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i) # 这是个什么玩意？
#       i += 1
#    return checker

# print(div_by_primes_under(10)(121))


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """

    def checker(x):
        return False

    i = 2
    while i <= n:
        if not checker(i):

            def outer(f, i):

                def inner(x):
                    return x % i == 0 or f(x)

                return inner

            checker = outer(checker, i)
        i += 1
    return checker


print(div_by_primes_under_no_lambda(10)(12))