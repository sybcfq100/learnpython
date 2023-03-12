#  def min_abs_indices(s):
#      min_abs = min(map(abs, s))
#      #  return [i for i in range(len(s)) if abs(s[i]) == min_abs]
#      f = lambda i: abs(s[i]) == min_abs
#      return list(filter(f, range(len(s))))
#  print(min_abs_indices([-4, -3, -2, 3, 2, 4]))
#
#  def largest_adj_sum(s):
#      return max(s[i] + s[i+1] for i in range(len(s) - 1))
#  print(largest_adj_sum([-4, -3, -2, 3, 2, 4]))
#
#
#  def digit_dict(s):
#      #  return {d: [x for x in s if x % 10 ==d] for d in range(10) if any([x % 10 == d for x in s])}
#      last_digits = [x % 10 for x in s]
#      return {d: [x for x in s if x % 10 ==d] for d in range(10) if d in last_digits}
#  print(digit_dict([5, 8, 13, 21, 34, 55, 89]))
#
#  def all_have_an_equal(s):
#      #  return all([s[i] in s[:i]+s[i+1:] for i in range(len(s))])
#      return min([s.count(x) for x in s]) > 1
#
#
#  print(all_have_an_equal([4, 3, 2, 3, 2, 4]))
#
#


""" link examples """
def ordered(s, key = lambda x: x):
    """is link s ordered?"""
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)

def merge(s, t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        #  return Link(s.first, merge(s.rest, t))
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        #  return Link(t.first, merge(s, t.rest))
        t.rest = merge_in_place(s, t.rest)
        return t
class Link:
    pass
