# 定义一个集合的操作类
# 包括的方法：
# 1.集合元素添加
# 2.集合元素的交集
# 3.集合元素的差集
# 4.集合元素的并集

class SetInfo():
    def __init__(self, s):
        self.s = s

    def add_value(self, v):
        self.s.add(v)
        return self.s

    def intersection_value(self, s2):
        # 取交集的另外一种方法是用 & 符号
        return self.s.intersection(s2)

    # return self.s & s2

    def difference_value(self, s2):
        # 取差集集的另外一种方法是用 - 符号
        return self.s.difference(s2)

    # return self.s - s2

    def union_value(self, s2):
        # 取交集的另外一种方法是用 | 符号
        return self.s.union(s2)
    # return self.s | s2


setinfo = SetInfo({1, 2, 3, 4, 5})

# print(setinfo.add_value(6))
# print(setinfo.s)
print(setinfo.difference_value({5, 7, 8}))