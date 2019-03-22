# 定义一个点（point）和直线（Line）类，使用getLen方法获取两点构成直线的长度
import math


# 需要用到该模块的平方根函数sqrt
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

    def getLen(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


p1 = Point(7, 3)
p2 = Point(6, 7)
line = Line(p1, p2)
print(line.getLen())
