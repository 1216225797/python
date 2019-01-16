'''
property函数使用案例
'''


class A():
    # 注意变量名称前的下划线，这个是必须的,不然会进入死循环报错
    def fget(self):
        return self._name * 2

    def fset(self,name):
        # 把获取到的姓名都转化为大写
        self.name = name.upper()

    def fdel(self):
        a.name =  "NoName"

    name = property(fget, fset, fdel, "对name属性进行操作啦~~")

a = A()
a.name = "gaoy"
# 所要进行的操作
print(a.name)


# 修改成员属性方法二
class B():
    def __init__(self,name):
        self.name = name
        self.setName(name)

    def hello(self):

        print("hello,{0}".format(self.name))


    def setName(self,name):
        
        name = name.upper()



b = B("xiaoguo")
b.hello()

print(A.__dict__)


# __call__函数举例

class C():
    def __init__(self,name):
        print("cccccc")
        self.setName(name)

    def __call__(self):
        print("hahah")
    '''
    def __str__(self):
        # return 和 print的区别
        # return 的内容需要print才能显示出来
        # return后面的程序将不再执行，比如打印一个1到5的for循环，如果使用return则只打印1，后面2,3,4,5不打印
        # print则1,2,3,4,5全部打印
        
         return "这里是str"
    '''
    def __repr__(self):

        return  "这里是repr"
    '''
    def __set__(self):
        print("修改属性了啊啊啊啊~~")
    '''
    def setName(self,name):
        self.name = name.upper()
        print(self.name)

    def __getattr__(self,attr):
        print("没找到")
        print(attr)
        return attr
c = C("xxii")
c()
print(c)
print(c.age)
