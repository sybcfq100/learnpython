def everything(n):
    if n == 0:
        return 0
    for rest in everything(n // 10):
        yield rest
        yield 10 * rest + n % 10


print(list(everything(98357)))


#  def increasing(n, smallest=10):
#      if n == 0:
#          return 0
#      elif n%10 < smallest:
#          no = increasing(n//10, smallest)
#          yes = increasing(n//10, min(n%10, smallest))*10 + n%10
#          return max(no, yes)
#      else:
#          return increasing(n//10, smallest)

# def close(n, smallest = 10, d = 10):
#     if n == 0:
#         return 0
#     no = close(n//10, smallest, d)
#     if smallest > n % 10:
#         yes = close(n//10, min(smallest, d), n %10 )*10 + n%10
#         return max(yes, no)space
#     return no

# print(close(45671))
