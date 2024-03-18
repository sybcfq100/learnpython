#  def average(x, y):

#      return (x + y) / 2
#
#
#  def improve(update, close, guess=1):
#      while not close(guess):
#          guess = update(guess)
#      return guess
#
#
#  def approx_eq(x, y, tolerance=1e-3):
#      return abs(x - y) < tolerance
#
#
#  def sqrt(a):
#      def sqrt_update(x):
#          return average(x, a / x)
#
#      def sqrt_close(x):
#          return approx_eq(x * x, a)
#
#      return improve(sqrt_update, sqrt_close)
#
#
#  result = sqrt(250)
#  print(result)
#  tag : how to use lambda
g = lambda x: lambda y: y + 1  # noqa: E731
eight = g(1)(7)
print(eight)
