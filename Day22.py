#  def apply_twice(f, x):
#      return f(f(x))
#
#  def f_square(x):
#      return x * x
#
#  print(apply_twice(f_square, 10))

# def repeat(f, x):
#     while f(x) != x:
#         x = f(x)
#     return x

# def g(y):
#     return (y + 5) // 3


# print(repeat(g, 5))

#  def make_adder(n):
#      def adder(k):
#          return k + n
#      return adder
#
#  def square(x):
#      return x * x
#
#  def triple(x):
#      return 3 * x
#
#  def compose1(f, g):
#      def h(x):
#          return f(g(x))
#      return h
#
#  print(compose1(triple, square)(5))

#  def print_sums(x):
    #  print(x)
    #  def next_sum(y):
    #      return print_sums(x+y)
    #  return next_sum
    #
#  print_sums(3)(4)(5)(6)

#  def f(x):
#      me = 1
#      def g(y):
#          return me
#      me = 2
#      print(g(7))
#      return x + y
#
#
#  y = 1
#  z = f(2)

#  def curry2(f):
#      def g(x):
#          def h(y):
#              return f(x, y)
#          return h
#      return g
#  # curried_pow = curry2(pow)
#  # two_to_the = curried_pow(2)
#
#  # x = two_to_the(5)
#  x = curry2(pow)(2)(5)
#  print(x)

# def square(x):
#     return x * x

# def make_adder(n):
#     def adder(k):
#         return n + k
#     return adder

# def compose1(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# print(compose1(square, make_adder(2))(3))

# higher_order_lambda = lambda f: lambda x: f(x)

# g = lambda x: x * x
# print(higher_order_lambda(g)(2))

#  def coffee(grounds):
#      x = 4
#      return grounds(x)
#  x = 6
#  print(coffee(lambda x: x + 10))
#  import matplotlib.pyplot as plt
#
#  l1 = []
#  for x in range(10):
#      g = lambda x: x**x
#      l1.append(g(x))
#
#  fig, ax = plt.subplots()
#  ax.plot(range(10), l1)
#  plt.show()

#  from operator import mul
#
#  def square(square):
#      return mul(square, square)
#
#  print(square(4))

from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    '''encode float x between -1 and 1 as two bytes'''
    i = int(16384*x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    '''write the output of a sampler function as a wav file'''
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude = 0.3):
    '''a continuous triangel wave.'''
    period = frame_rate //frequency
    def sampler(t):
        saw_wave = t / period - floor(t/period + 0.5)
        tri_wave = 2*abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler
c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f, g):
    return lambda t: f(t) + g(t)
#  play(both(tri(c_freq), tri(e_freq)))
def note(f, start, end, fade = 0.1):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start)/fade*f(t)
        elif seconds > end -fade:
            return (end-seconds)/fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave):
    c, e = tri(octave*c_freq), tri(octave*e_freq)
    g, low_g = tri(octave*g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song
play(both(mario_at(1), mario_at(1/2)))
