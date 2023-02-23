#  """
#  经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
#  """
#  from enum import Enum, unique
#
#  import random
#
#
#  @unique
#  class Suite(Enum):
#      """花色"""
#
#      SPADE, HEART, CLUB, DIAMOND = range(4)
#
#      def __lt__(self, other):
#          return self.value < other.value
#
#
#  class Card():
#      """牌"""
#      def __init__(self, suite, face):
#          """初始化方法"""
#          self.suite = suite
#          self.face = face
#
#      def show(self):
#          """显示牌面"""
#          suites = ['♠︎', '♥︎', '♣︎', '♦︎']
#          faces = [
#              '', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
#              'K'
#          ]
#          return f'{suites[self.suite.value]}{faces[self.face]}'
#
#      def __repr__(self):
#          return self.show()
#
#
#  class Poker():
#      """扑克"""
#      def __init__(self):
#          self.index = 0
#          self.cards = [
#              Card(suite, face) for suite in Suite for face in range(1, 14)
#          ]
#
#      def shuffle(self):
#          """洗牌（随机乱序）"""
#          random.shuffle(self.cards)
#          self.index = 0
#
#      def deal(self):
#          """发牌"""
#          card = self.cards[self.index]
#          self.index += 1
#          return card
#
#      @property
#      def has_more(self):
#          return self.index < len(self.cards)
#
#
#  class Player():
#      """玩家"""
#      def __init__(self, name):
#          self.name = name
#          self.cards = []
#
#      def get_one(self, card):
#          """摸一张牌"""
#          self.cards.append(card)
#
#      def sort(self, comp=lambda card: (card.suite, card.face)):
#          """整理手上的牌"""
#          self.cards.sort(key=comp)
#
#
#  def main():
#      """主函数"""
#      poker = Poker()
#      poker.shuffle()
#      players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#      while poker.has_more:
#          for player in players:
#              player.get_one(poker.deal())
#      for player in players:
#          player.sort()
#          print(player.name, end=': ')
#          print(player.cards)
#
#
#  if __name__ == '__main__':
#  main()

#  from math import pi, sqrt
#
#
#  def area(r, shape_constant):
#      assert r > 0, 'A length must be positive'
#      return r * r * shape_constant
#
#
#  def area_square(r):
#      return area(r, 1)
#
#
#  def area_circle(r):
#      return area(r, pi)
#
#
#  def area_hexagon(r):
#      return area(r, 3 * sqrt(3) / 2)
from operator import mul
'''Generalization.'''


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)


def summation(n, term):
    '''sum the first N terms of a sequence.'''

    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    '''sum the first N natural numbers.
    >>> sum_naturals(5)
    15
    '''
    return summation(n, identity)


def sum_pi(n):
    return summation(n, pi_term)


def sum_cubes(n):
    '''sum the first N cube numbers.
    >>> sum_cubes(5)
    225
    '''
    return summation(n, cube)


print(sum_naturals(5))
print(sum_cubes(5))
print(sum_pi(100000))
