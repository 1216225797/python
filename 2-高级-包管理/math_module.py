'''
常用内置模块
math篇

'''
# 数学运算模块
import math

print(type(math))

# 向上取整 celi()
print(math.ceil(5.2))

# 向下取整 floor()
s = math.floor(5.2)
print(s)

# 查看系统保留关键字模块
import keyword
print(keyword.kwlist)

# 内置函数，四舍五入 round()
print(round(3.2))
print(round(3.9))

# 开平方，返回浮点数 sqrt()
m = math.sqrt(3)
print(m)
# 结果打印为整数
# print(int(m))


# pow() 计算一个数的几次方，有两个参数，一个是底数，一个是指数，返回浮点数
print(math.pow(2,3))
# 内置函数pow()可以传递三个参数，除了上面两个外，第三个是取余参数(可选)，返回整数
print(pow(3,2,5)) # 等于print(3 ** 2 % 4)

# fabs() 获取绝对值，返回浮点数
print(math.fabs(-9))

# abs() 获取绝对值，内置函数，返回值类型由结果类型而定
# abs()

'''
可迭代对象：
给定一个list或者tuple，通过for循环来遍历这个list或者tuple、这种遍历就是迭代（iteration）。

'''

# 只要是可迭代的对象都可以进行迭代、怎么判断一个对象是否是可迭代的对象呢？
# 可以用collections模块里面的iterable包的isinstance函数进行判断：
# 需要导入collection模块下面的Iterable
from collections import Iterable

print(isinstance([],Iterable)) # 判断列表是否是可迭代对象
print(isinstance('',Iterable)) # 判断字符串是否是可迭代对象
print(isinstance((),Iterable)) # 判断元组是否是可迭代对象
print(isinstance({},Iterable)) # 判断集合是否是可迭代对象


# fsum() 对整个序列求和，返回浮点数,必须是可迭代对象
# 求1-100整数的和
def Sum():
    l = list()
    for i in range(100):
        l.append(i)

    print(math.fsum(l))
Sum()


# sum() 内置求和函数，返回值类型由结果类型决定
print(sum([1,2,7]))


# modf() 将一个浮点数拆分为整数部分和小数部分并组成元组，小数部分在前，整数部分在后,结果均为浮点型
print(math.modf(0))
print(math.modf(1))
print(math.modf(3.4)) # 为什么小数部分不是0.4?

# copysign() 将第二个参数的正负号传给第一个参数，返回第一个参数，结果为浮点数
print(math.copysign(1,-2))