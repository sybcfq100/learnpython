#  HW_SOURCE_FILE = __file__

# def num_eights(n):
#  """Returns the number of times 8 appears as a digit of n.
#
#  >>> num_eights(3)
#  0
#  >>> num_eights(8)
#  1
#  >>> num_eights(88888888)
#  8
#  >>> num_eights(2638)
#  1
#  >>> num_eights(86380)
#  2
#  >>> num_eights(12345)
#  0
#  >>> num_eights(8782089)
#  3
#  >>> from construct_check import check
#  >>> # ban all assignment statements
#  >>> check(HW_SOURCE_FILE, 'num_eights',
#  ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
#  True
#  """
# count = 0
# for _ in range(len(str(n))):
#     if n % 10 == 8:
#         count += 1
#     n = n // 10
# return count

#
#  print(num_eights(123456))

#  def pingpong(n):
#      """Return the nth element of the ping-pong sequence.
#
#      >>> pingpong(8)
#      8
#      >>> pingpong(10)
#      6
#      >>> pingpong(15)
#      1
#      >>> pingpong(21)
#      -1
#      >>> pingpong(22)
#      -2
#      >>> pingpong(30)
#      -2
#      >>> pingpong(68)
#      0
#      >>> pingpong(69)
#      -1
#      >>> pingpong(80)
#      >>> pingpong(81)
#      1
#      >>> pingpong(82)
#      0
#      >>> pingpong(100)
#      -6
#      >>> from construct_check import check
#      >>> # ban assignment statements
#      >>> check(HW_SOURCE_FILE, 'pingpong',
#      ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
#      True
#      """
#
#      def helper(result, i, step=1):
#          if i == n:
#              return result
#          # elif i % 8 == 0 or num_eights(i) > 0:
#          elif i % 8 == 0 or "8" in str(i):
#              return helper(result - step, i + 1, -step)
#          else:
#              return helper(result + step, i + 1, step)
#
#      return helper(1, 1)
#
#
#  print(pingpong(10))
#

# Alternate solution 1
# def pingpong_next(x, i, step):
#     if i == n:
#         return x
#     return pingpong_next(x + step, i + 1, next_dir(step, i + 1))

# def next_dir(step, i):
#     if i % 8 == 0 or num_eights(i) > 0:
#         return -step
#     return step

#     i = 1
#     x = 1
#     is_up = True
#     while i < n:
#         is_up = next_dir(is_up, i)
#         if is_up:
#             x += 1
#         else:
#             x -= 1
#         i += 1
#     return x

# def next_dir(is_up, i):
#     # if i % 8 == 0 or num_eights(i) > 0:
#     if i % 8 == 0 or '8' in str(i):
#         return not is_up
#     return is_up

# print(pingpong(100))

# def next_larger_coin(coin):
#     """Returns the next larger coin in order.
#     >>> next_larger_coin(1)
#     5
#     >>> next_larger_coin(5)
#     10
#     >>> next_larger_coin(10)
#     25
#     >>> next_larger_coin(2) # Other values return None
#     """
#     if coin == 1:
#         return 5
#     elif coin == 5:
#         return 10
#     elif coin == 10:
#         return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    #     """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    #     >>> count_coins(15)
    #     6
    #     >>> count_coins(10)
    #     4
    #     >>> count_coins(20)
    #     9
    #     >>> count_coins(100) # How many ways to make change for a dollar?
    #     242
    #     >>> count_coins(200)
    #     1463
    #     >>> from construct_check import check
    #     >>> # ban iteration
    #     >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    #     True
    #     """

    # def constrained_count(change, smallest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if smallest_coin is None:
    #         return 0
    #     with_coin = constrained_count(change-smallest_coin, smallest_coin)
    #     without_coin = constrained_count(change, next_larger_coin(smallest_coin))
    #     return without_coin + with_coin

    # return constrained_count(change, 1)
    def constrained_count(change, largest_coin):
        """_summary_

        Parameters
        ----------
        change : _type_
            _description_
        largest_coin : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        if change == 0:
            return 1
        if change < 0:
            return 0
        if largest_coin is None:  # or None can be used as a flag value.  It is not a valid value.  None is a valid value
            return 0

        without_coin = constrained_count(change,
                                         next_smaller_coin(largest_coin))
        with_coin = constrained_count(change - largest_coin, largest_coin)

        return with_coin + without_coin

    return constrained_count(change, 25)


print(count_coins(10))
