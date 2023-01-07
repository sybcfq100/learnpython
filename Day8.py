# class Student(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         print(f'{self.name} is learning {course_name}.')
#         # print('%s is learning %s.' %(self.name, course_name))

#     def watch_movie(self):
#         if self.age < 18:
#             print(f'{self.name} only can see <Beer>.')
#         else:
#             print(f'{self.name} is watching act movie.')


# def main():  # sourcery skip: extract-duplicate-method
#     stu1 = Student('Wayne', 38)
#     stu1.study('Python')
#     stu1.watch_movie()
#     stu2 = Student('David', 18)
#     stu2.study('Physic')
#     stu2.watch_movie()

# if __name__=='__main__':
#     main()


# from time import sleep

# class Clock(object):

#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     def run(self):
#         self._second = self._second + 1
#         if self._second == 60:
#             self._second = 0
#             self._minute +=  1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour +=  1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__=='__main__':
#     main()


from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y
        
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return f'({str(self.x)}, {str(self.y)})'

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__=='__main__':
    main()
