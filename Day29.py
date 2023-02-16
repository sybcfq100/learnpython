
#  def add_chars(w1, w2):
#      if len(w1) > len(w2):
#          w1, w2 = w2, w1
#      if len(w1) == 0:
#          return w2
#      if w1[0] == w2[0]:
#          return add_chars(w1[1:], w2[1:])
#      else:
#          return w2[0] + add_chars(w1, w2[1:])
#
#  w2 = 'arp'
#  w1 = 'appear'
#  print(add_chars(w1, w2))

# g = lambda n: (lambda f: f(n, f))(lambda n, fact: 1 if n ==1 else n * fact(n-1, fact))
# print(g(4))
a1 = min([3,2,5,6])
print(a1)

a2 = min([3,2,5,6], key=lambda x: abs(x*x-24))
print(a2)
f = lambda x: abs(x*x-24)
t = [f(x) for x in [3,2,5,6]]
print(t)
d = [[f(x),x] for x in [3,2,5,6]]
md = min(d)
print(md)
