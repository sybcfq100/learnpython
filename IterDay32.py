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
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


if __name__=="__main__":
    print(fib(5))
    print(fib(10))