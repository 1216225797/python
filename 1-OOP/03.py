'''
知识点案例
'''

# 继承的语法
# 在Python中，任何类都有一个共同的父类叫object
class A():
    name = "Tom"
    age = 6
    def eat(self):
        print("My name is {0}, and i am {1} years old".format(self.name,self.age))

class B(A):
    name = "jerry"
    _stature = 130
    def play(self):
        print("I am very very like play basketball")

    def xx(self):
        # 父类成员方法扩充
        # 注意传值，这里self代表子类，所以子类可以充当父类，反之则不行
        # 方法一
        A.eat(self)
        # 方法二
        super().eat()
        print(self._stature)
b = B()
b.xx()


