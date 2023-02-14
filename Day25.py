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
''' it's the function to replace f_then_g and grow and shrink'''
# def grow(n):
#     if n // 10 != 0:
#         grow(n // 10)
#         print(n//10)


# def shrink(n):
#     if n // 10!= 0:
#         print(n//10)
#         shrink(n // 10)


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
''' another expression for fib number.'''
def fact(n):
    return fact_times(n, 1)

def fact_times(n,k):
    '''return k*n*(n-1)*...*1'''
    if n == 0:
        return k
    else:
        return fact_times(n-1, k*n)


'''
Q(n,m)=Q(n,m-1)+Q(n-m,m),
等式右边第一部分Q(n,m-1)表示被加数不包含m的分划的数目，
第二部分表示被加数中包含（注意不是小于）m的分划的数目，
因为如果确定了一个分划的被加数中包含m,则剩下的部分就是对n-m进行不超过m的划分。
以5，3为例：
分为包涵3的分类：剩下5-3=2，可将2分划，且分划最大值不超过3

'''
def trace(f):
    def g(n, m):
        print(f'{f.__name__}({str(n)}, {str(m)}) was called')
        result  =f(n ,m)
        print(f'{f.__name__}({str(n)}, {str(m)}) => {str(result)}')

        return result
    return g

@trace
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, min(m, n-m))
        without_m = count_partitions(n, m-1)
        return with_m + without_m

print(count_partitions(6, 4))
