# 定义一个列表的操作类
# 包括的方法：
# 1.列表元素添加，添加的数据必须是整数或者字符串
# 2.列表元素取值
# 3.列表合并
# 4.删除并且返回最后一个元素
class ListInfo():
    def __init__(self, l):
        self.l = l

    def list_add(self, k):
        # 内建函数isinstance()：检测一个对象是否是另一个类的实例
        if isinstance(k, (int, str)):
            self.l.append(k)
            return self.l
        return "请添加整数或者字符串"

    def list_get(self, i):
        if i < 0 or i > len(self.l) - 1:
            return "没有该值"
        return self.l[i]

    def list_merge(self, l2):
        # 这个地方也可以用list列表的extend()函数
        # self.l.extend(l2)
        return self.l + l2

    def del_values(self):
        if len(self.l) > 0:
            return self.l.pop()
        return "已经没有可以删除的数据了"


listinfo = ListInfo([1, 2, 3, 4, 5])

print(listinfo.list_add('xaaa'))
