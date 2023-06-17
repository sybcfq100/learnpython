#  def count(s, value):
#  #      total, index = 0, 0
#      #  while index < len(s):
#      #      element = s[index]
#      #
#      #      if element == value:
#      #          total += 1
#      #
#      #      index += 1
#  #      return total
#      total = 0
#      for element in s:
#          if element == value:
#              total += 1
#      return total
#
#  print(count([1,2,1,2,1],1))
#  pairs = [[1,2], [2,2], [3,2], [4,4]]
#  same_count = 0
#  for x, y in pairs:
#      if x == y:
#          same_count += 1
#
#  print(same_count)
#
#  def sum_iter(n):
#  sum = 0
#  for i in range(n+1):
#      sum += i
#
#  return sum
#
#  print(sum_iter(5))

#  def sum_rec(n):
#  if n == 0:
#      return 0
#  else:
#      return n + sum_rec(n-1)
#
#  print(sum_rec(5))

#  def divsions(n):
#  return [x for x in range(1, n) if n%x==0]
#
#  print(divsions(12))

#  def reverse(s):
#      if s == '':
#          return s
#  #      if len(s) == 1:
#  #          return s
#      return reverse(s[1:]) + s[0]
#
#  print(reverse('hello'))
