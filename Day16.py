#  生成式（推导式）的用法
#  prices = {
#          'AAPL': 191.88,
#          'GOOG': 1186.96,
#          'IBM': 149.24,
#          'ORCL': 48.44,
#          'FB': 208.09,
#          'SYMC': 211.29
#          }
#  prices2 = {key: value for key, value in prices.items() if value > 100}
#  print(prices2)

#  嵌套的列表

#  names = ['guan', 'zhang', 'zhao', 'ma', 'huang'#  ]
#  courses = ['chinese', 'math', 'english']
#
#  scores = [[None] * len(courses) for _ in range(len(names))]
#
#  for row, name in enumerate(names):
#      for col, course in enumerate(courses):
#          scores[row][col] = float(input(f'please inter {name} of {course}: '))
#  print(scores)

#  #  heapq 模块 (堆排序)
#  '''
#  从列表中找出最大或最小的N个元素
#  堆结构
#  '''
#  import heapq
#
#  list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
#  print(heapq.nlargest(3, list1))

#  itertools 模块
#  import itertools

#  for _ in #  itertools.permutations('ABCD'):
#  print(_)
# b = itertools.combinations('ABCDE', 3)
#  for  _ in itertools.combinations('ABCDE', 3):
#  print(_)

#  for _ in itertools.product('ABC', '123'):
#  print(_)
#  产生ABC的无限循环序列
#  for _ in itertools.cycle(('A', 'B', 'C')):
#  print(_)
#  """
#  找出序列中出现次数最多的元素
#  """
#  from collections import Counter
#
#  words = [
#      'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
#      'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
#      'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
#      'under'
#  ]
#  counter = Counter(words)
#  print(counter.most_common(3))
#


#  排序算法--选择
#  def select_sort(items, comp=lambda x, y: x < y):
#  items = items[:]
#  for i in range(len(items) - 1):
#      min_index = i
#      for j in range(i + 1, len(items)):
#          if comp(items[j], items[min_index]):
#              min_index = j
#      items[i], items[min_index] = items[min_index], items[i]
#  return items
#
#  排序算法--冒泡
#  def bubble_sort(items, comp=lambda x, y: x > y):
#      items = items[:]
#      for i in range(len(items) - 1):
#          swapped = False
#          for j in range(len(items) - 1 - i):
#              if comp(items[j], items[j + 1]):
#                  items[j], items[j + 1] = items[j + 1], items[j]
#                  swapped = True
#          if not swapped:
#              break
#      return items
#
#
#  搅拌排序 冒泡排序的升级版
#  def bubble_sort(items, comp=lambda x, y: x > y):
#      items = items[:]
#      for i in range(len(items) - 1):
#          swapped = False
#          for j in range(len(items) - 1 - i):
#              if comp(items[j], items[j + 1]):
#                  items[j], items[j + 1] = items[j + 1], items[j]
#                  swapped = True
#
#          if swapped:
#              swapped = False
#              for j in range(len(items) - 2 - i, i, -2):
#                  if comp(items[j - 1], items[j]):
#                      items[j], items[j - 1] = items[j - 1], items[j]
#                      swapped = True
#          if not swapped:
#              break
#      return items
# def merge(items1, items2, comp=lambda x, y: x < y):
#     """合并(将两个有序的列表合并成一个有序的列表)"""
#     items = []
#     index1, index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 += 1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items


# def merge_sort(items, comp=lambda x, y: x < y):
#     return _merge_sort(list(items), comp)


# def _merge_sort(items, comp):
#     """归并排序"""
#     if len(items) < 2:
#         return items
#     mid = len(items) // 2
#     left = _merge_sort(items[:mid], comp)
#     right = _merge_sort(items[mid:], comp)
#     return merge(left, right, comp)

# a = [3, 25, 38, 53, 82, 95]
# b = [14, 35, 48, 60, 72, 85]

# #  print(select_sort(a))
# #  print(bubble_sort(a))
# print(merge(a, b))

# def seq_search(items, key):
#     '''顺序查找'''
#     for index, item in enumerate(items):
#         return index if item == key else -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1