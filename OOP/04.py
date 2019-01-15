'''
学习案例
'''


class A():
    def fget(self):
        return self.name

    def fset(self,name):
        self.name = name.upper()

    def fdel(self):
        self.name = "NoName"


    name = property(fget,fset,fdel,"对name属性进行操作啦~~")

a = A()
a.name="gaoyuan"
# 所要进行的操作
print(a.name)