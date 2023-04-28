#  def falling(n, k):
#  """Compute the falling factorial of n to depth k.
#
#  >>> falling(6, 3)  # 6 * 5 * 4
#  120
#  >>> falling(4, 3)  # 4 * 3 * 2
#  24
#  >>> falling(4, 1)  # 4
#  4
#  >>> falling(4, 0)
#  1
#  """
#  "*** YOUR CODE HERE ***"
#
#  if k == 0:
#      return 1
#  else:
#      return falling(n - 1, k - 1) * n
#
#
#  print(falling(6, 3))

#  def divisible_by_k(n, k):
#  """
#  >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
#  2
#  4
#  6
#  8
#  10
#  >>> a
#  5
#  >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
#  1
#  2
#  3
#  >>> b
#  3
#  >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
#  >>> c
#  0
#  """
#  "*** YOUR CODE HERE ***"
#  count = 0
#  if n < k:
#      return 0
#  else:
#      for i in range(1, n + 1):
#          if i % k == 0:
#              print('>>> {}'.format(i))
#              count += 1
#              i += 1
#      return count
#
#
#  print(divisible_by_k(15, 3))

#  def sum_digits(y):
#      """Sum all the digits of y.
#
#      >>> sum_digits(10) # 1 + 0 = 1
#      1
#      >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
#      12
#      >>> sum_digits(1234567890)
#      45
#      >>> a = sum_digits(123) # make sure that you are using return rather than print
#      >>> a
#      6
#      """
#      "*** YOUR CODE HERE ***"
#
#      if y // 10 == 0:
#          return y % 10
#      else:
#          return y % 10 + sum_digits(y // 10)
#
#
#  print(sum_digits(123))
#


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # if n % 100 == 88:
    #     return True
    # else:
    #     for _ in range(len(str(n)) - 1):
    #         n = n // 10
    #         #  print(n)
    #         if n % 100 == 88:
    #             return True
    # return False
    " *** answor code "
    prev_eight = False  # 0 is not a digit.  0 is also the first digit.  So the first digit is not counted.  So the first
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10  # checking if the last di
    return False


print(double_eights(880088))
