# import itertools
# for x, y in itertools.product(range (20), range(33)):
#     z = 100-x-y
#     if 5*x + 3*y + z//3 == 100 and z % 3 ==0:
#         print(x, y ,z)

#  fish = 6
#  while True:
#      total = fish
#      enough = True
#      for _ in range(5):
#          if (total - 1) % 5 == 0:
#              total = (total - 1) // 5 * 4
#          else:
#              enough = False
#              break
#      if enough:
#          print(fish)
#          break
#      fish += 5
#  #
#  """
#  贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
#  输入：
#  20 6
#  电脑 200 20
#  收音机 20 4
#  钟 175 10
#  花瓶 50 2
#  书 10 1
#  油画 90 9
#  """
#
#
#  class Thing(object):
#      def __init__(self, name, price, weight):
#          self.name = name
#          self.price = price
#          self.weight = weight
#
#      @property
#      def value(self):
#          return self.price / self.weight
#
#
#  def input_thing():
#      name_str, price_str, weight_str = input().split()
#      return name_str, int(price_str), int(weight_str)
#
#
#  def main():
#      max_weight, num_of_things = map(int, input().split())
#      all_things = []
#      for _ in range(num_of_things):
#          all_things.append(Thing(*input_thing()))
#      all_things.sort(key=lambda x: x.value, reverse=True)
#      total_weight = 0
#      total_price = 0
#      for thing in all_things:
#          if total_weight + thing.weight <= max_weight:
#              print(f'小偷拿走了{thing.name}')
#              total_weight += thing.weight
#              total_price += thing.price
#      print(f'总价值: {total_price}美元')
#
#
#  if __name__ == '__main__':
#  main()
# """
#  快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
#  """
#
#
#  def quick_sort(items, comp=lambda x, y: x <= y):
#      items - list(items)[:]
#      _quick_sort(items, 0, len(items) - 1, comp)
#      return items
#
#
#  def _quick_sort(items, start, end, comp):
#      if start < end:
#          pos = _partition(items, start, end, comp)
#          _quick_sort(items, start, pos - 1, comp)
#          _quick_sort(items, pos + 1, end, comp)
#
#
#  def _partition(items, start, end, comp):
#      pivot = items[end]
#      i = start - 1
#      for j in range(start, end):
#          if comp(items[j], pivot):
#              i += 1
#              items[i], items[j] = items[j], items[i]
#      items[i + 1], items[end] = items[end], items[i + 1]
#  return i + 1
#  """
#  递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
#  """
#  import sys
#  import time
#
#  SIZE = 5
#  total = 0
#
#
#  def print_board(board):
#      for row in board:
#          for col in row:
#              print(str(col).center(4), end='')
#          print()
#
#
#  def patrol(board, row, col, step=1):
#      if row >= 0 and row < SIZE and \
#          col >= 0 and col < SIZE and \
#          board[row][col] == 0:
#          board[row][col] = step
#          if step == SIZE * SIZE:
#              global total
#              total += 1
#              print(f'第{total}种走法: ')
#              print_board(board)
#          patrol(board, row - 2, col - 1, step + 1)
#          patrol(board, row - 1, col - 2, step + 1)
#          patrol(board, row + 1, col - 2, step + 1)
#          patrol(board, row + 2, col - 1, step + 1)
#          patrol(board, row + 2, col + 1, step + 1)
#          patrol(board, row + 1, col + 2, step + 1)
#          patrol(board, row - 1, col + 2, step + 1)
#          patrol(board, row - 2, col + 1, step + 1)
#          board[row][col] = 0
#
#
#  def main():
#      board = [[0] * SIZE for _ in range(SIZE)]
#      patrol(board, SIZE - 1, SIZE - 1)
#
#
#  if __name__ == '__main__':
#      main()
#
#  def main():
#      items = list(map(int, input().split()))
#      overall = partial = items[0]
#      for i in range(1, len(items)):
#          partial = max(items[i], partial + items[i])
#          overall = max(partial, overall)
#      print(overall)
#
#
#  if __name__ == '__main()__':
#      main()
#  item1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
#  print(item1)
#  item2 = [x ** 2 for x in range(1, 10) if x % 2#  ]
#  print(item2)
