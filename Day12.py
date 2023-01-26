# class Student:

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def study(self, course_name):
#         print(f'{self.__name}正在学习{course_name}.')

# stu = Student('王大锤', 20)
# stu.study('Python程序设计')
# print(stu._Student__name, stu._Student__age)

# class Person:
#     """人类"""

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f'{self.name}正在吃饭.')

#     def sleep(self):
#         print(f'{self.name}正在睡觉.')

# class Student(Person):
#     """学生类"""

#     def __init__(self, name, age):
#         # super(Student, self).__init__(name, age)
#         super().__init__(name, age)

#     def study(self, course_name):
#         print(f'{self.name}正在学习{course_name}.')

# class Teacher(Person):
#     """老师类"""

#     def __init__(self, name, age, title):
#         # super(Teacher, self).__init__(name, age)
#         super().__init__(name, age)
#         self.title = title

#     def teach(self, course_name):
#         print(f'{self.name}{self.title}正在讲授{course_name}.')

# stu1 = Student('白元芳', 21)
# stu2 = Student('狄仁杰', 22)
# teacher = Teacher('武则天', 35, '副教授')
# stu1.eat()
# stu2.sleep()
# teacher.teach('Python程序设计')
# stu1.study('Python程序设计')

#  class Person:
#      """人类"""
#
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#
#      def eat(self):
#          print(f'{self.name}正在吃饭.')
#
#      def sleep(self):
#          print(f'{self.name}正在睡觉.')
#
#
#  class Student(Person):
#      """学生类"""
#
#      def __init__(self, name, age):
#          # super(Student, self).__init__(name, age)
#          super().__init__(name, age)
#
#      def study(self, course_name):
#          print(f'{self.name}正在学习{course_name}.')
#
#
#  class Teacher(Person):
#      """老师类"""
#
#      def __init__(self, name, age, title):
#          # super(Teacher, self).__init__(name, age)
#          super().__init__(name, age)
#          self.title = title
#
#      def teach(self, course_name):
#          print(f'{self.name}{self.title}正在讲授{course_name}.')
#
#
#
#  stu1 = Student('白元芳', 21)
#  stu2 = Student('狄仁杰', 22)
#  teacher = Teacher('武则天', 35, '副教授')
#  stu1.eat()
#  stu2.sleep()
#  teacher.teach('Python程序设计')
#  stu1.study('Python程序设计')

#  from enum import Enum
#
#  class Suite(Enum):
#      '''花色（枚举）'''
#      SPACE, HEART, CLUB, DIAMOND = range(4)
#
#
#  class Card:
#      '''牌'''
#      def __init__(self, suite, face):
#          self.suite = suite
#          self.face = face
#
#      def __repr__(self):
#          suites = '♠♥♣♦'
#          faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#          return f'{suites[self.suite.value]}{faces[self.face]}'
#      def __lt__(self, other):
#          if self.suite == other.suite:
#              return self.face < other.face
#          return self.suite.value < other.suite.value
#
#  import random
#  ''' poker '''
#
#  class Poker:
#      def __init__(self):
#          self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
#          self.current = 0
#
#      def shuffle(self):
#          ''' 洗牌 '''
#          self.current = 0
#          random.shuffle(self.cards)
#
#      def deal(self):
#          '''发牌'''
#          card = self.cards[self.current]
#          self.current+=1
#          return card
#
#      @property
#      def has_next(self):
#          '''还有没有牌可以发'''
#  class Player:
#
#      def __init__(self, name):
#          self.name = name
#          self.cards = []
#
#      def get_one(self, card):
#          self.cards.append(card)
#
#      def arrange(self):
#          self.cards.sort()
#
#  poker = Poker()
#  poker.shuffle()
#  players = [Player('东邪'), Player('西毒'),Player('南帝'),Player('北丐')]
#  for _ in range(13):
#      for player in players:
#          player.get_one(poker.deal())
#  for player in players:
#      player.arrange()
#      print(f'{player.name}: ', end='')
#  print(player.cards)
#  ''' 工薪发放系统 '''

#  from abc import ABCMeta, abstractmethod
#
#
#  class Employee(metaclass=ABCMeta):
#      '''员工（抽象类）'''
#      def __init__(self, name):
#          self.name = name
#
#      @abstractmethod
#      def get_salary(self):
#          '''结算月薪（抽象方法）'''
#          pass
#
#
#  class Manager(Employee):
#      '''部门经理'''
#      def get_salary(self):
#          return 15000.0
#
#
#  class Programmer(Employee):
#      '''程序员'''
#      def __init__(self, name, working_hour=0):
#          self.working_hour = working_hour
#          super().__init__(name)
#
#      def get_salary(self):
#          return 200.0 * self.working_hour
#
#
#  class Salesman(Employee):
#      '''销售员'''
#      def __init__(self, name, sales=0.0):
#          self.sales = sales
#          super().__init__(name)
#
#      def get_salary(self):
#          return 1800.0 + self.sales * 0.05
#
#
#  class EmployeeFactory:
#      '''创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合'''
#      @staticmethod
#      def create(emp_type, *args, **kwargs):
#          '''创建员工'''
#          all_epm_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
#          cls = all_epm_types[emp_type.upper()]
#          return cls(*args, **kwargs) if cls else None
#
#
#  def main():
#      '''主函数'''
#      emps = [
#          EmployeeFactory.create('M', '曹操'),
#          EmployeeFactory.create('P', '荀彧', 120),
#          EmployeeFactory.create('P', '郭嘉', 85),
#          EmployeeFactory.create('S', '典韦', 123000),
#      ]
#      for emp in emps:
#          print(f'{emp.name}: {emp.get_salary():.2f}元')
#
#
#  if __name__ == '__main__':
#      main()
#  from collections import Counter
#
#  words = [
#      'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#      'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#      'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#      'look', 'into', 'my', 'eyes', "you're", 'under'
#  ]
#  counter = Counter(words)
#  # 打印words列表中出现频率最高的3个元素及其出现次数
#  for elem, count in counter.most_common(3):
#      print(elem, count)
#
