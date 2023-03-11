# def double(x):
#     print('**', x, '=>', 2*x, '**')
#     return 2*x


# m = map(double, range(3, 7))
# f = lambda y: y >= 10
# t = filter(f, m)
# print(next(t))

# print(list(filter(f, map(double, range(3, 7)))))

# def evens(start, end):
#     even = start + start % 2
#     while even < end:
#         yield even
#         even += 2

# print(list(evens(1, 10)))

#  def countdown(k):
#      if k > 0:
#          yield k
#          yield from countdown(k-1)
#      else:
#          yield 'Blast off'
#
#  def prefixes(s):
#      if s:
#          yield from prefixes(s[:-1])
#          yield s
#
#  def substrings(s):
#      if s:
#          yield from prefixes(s)
#          yield from substrings(s[1:])
#
#  print(list(substrings('tops')))
#
#  from typing import Dict
#  memo: Dict[int, int] = {0: 0, 1: 1}
#
#  # def fib(n: int) -> int:
#  def fib(n):
#      if n not in memo:
#          memo[n] = fib(n-1) + fib(n-2)
#      return memo[n]
#
#
#  if __name__=="__main__":
#      print(fib(5))
    #  print(fib(10))

def interval(a, b):
    return [a, b]

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

<<<<<<< HEAD
#  a= interval(-1, 1)
#  b =interval(-2, 0)
#  print(mul_interval(a, b))
print(mul_interval(interval(-1, 1.5), interval(-2, 0)))
=======
if __name__=="__main__":
    print(fib(5))
    print(fib(10))
>>>>>>> 0e18016088a330dde3669e9b118d9c805de546d2
