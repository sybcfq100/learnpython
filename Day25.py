#  def cascade(n):
#      if n < 10:
#          print(n)
#      else:
#          print('before', n)
#          cascade(n // 10)
#          print('after', n)
#
#  print(cascade(321))
#

#  def cascade(n):
    #  print(n)
    #  if n > 10:
    #      cascade(n//10)
    #      print(n)
    #
    #
#  print(cascade(321))

#  def inverse_cascade(n):
#      grow(n)
#      print(n)
#      shrink(n)
#
#  def f_then_g(f, g, n):
#      if n:
#          f(n)
#          g(n)
#
#
#  grow = lambda n: f_then_g(grow, print, n//10)
#  shrink = lambda n: f_then_g(print, shrink, n//10)
#
#  print(inverse_cascade(1234))

#  def fib(n):
    #  if n == 0:
    #      return 0
    #  elif n == 1:
    #      return 1
    #  else:
    #      return fib(n-2) + fib(n-1)
    #
#  print(fib(7))


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

print(count_partitions(5, 3))
