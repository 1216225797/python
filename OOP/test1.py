# 定义一个字典类,完成如下功能
# 1.删除某个key
# 2.判断某个键是否在字典里,如果在则返回对应的值，不在则返回'not found'
# 3.返回键组成的列表，返回类型list
# 4.合并字典，并且返回合并后字典的values组成的列表，返回类型list

class DictCls():

    def __init__(self, d):
        self.d = d

    def del_key(self, k):
        if k not in self.d:
            return "没有该键"
        else:
            del self.d[k]
            print(self.d)
            return "删除成功"

    def get_dict(self, k):
        if k in self.d:
            return self.d[k]

        return 'not found'

    def get_key(self):
        list_key = list(self.d.keys())
        return list_key

    def update_dict(self, d2):
        # 字典合并的四种方法
        # 1.dict(d1.items() + d2.items())
        # 2.dict(d1, **d2)     方法2比方法1效率快
        # 3.d3 = {}
        #   d3.update(d1)
        #   d3.update(d2)
        d3 = {}
        d3.update(self.d)
        d3.update(d2)
        list_values = tuple(d3.values())
        return list_values


dc = DictCls({'c': 3, 'd': 4, 'e': 5})

# print(dc.del_key('c'))
print(dc.get_dict('f'))
# print(dc.d)
# print(dc.get_key('c'))
# print(dc.update_dict({'a':1,'b':2,'c':3}))