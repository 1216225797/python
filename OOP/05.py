'''
课程案例
'''

# 类和对象的三种方法
class Person():

    # 实例方法
    def run(self):
        print(self)
        print('runing......')

    # 静态方法
    # 不用第一个参数表示自身或者类
    # 需要声明
    @staticmethod
    def look():

        print('looking...')

    # 类方法
    # 第一个参数一般用cls表示，区别于self
    # 同样需要声明
    @classmethod
    def say(cls):
        print(cls)
        print('saying...')

p = Person()
# 实例方法
p.run()
p.look()
p.say()
print('*' * 50)
# 静态方法
Person.look()
print('#' * 50)

# 类方法
Person.say()

help(Person)