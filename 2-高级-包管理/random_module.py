'''

常用内置函数
random篇

'''

import random

# random() 获取0-1之间的随机小数，包含0不包含1
# randint() 获取指定数值之间的随机整数，左右都包含
# rnadrange() 获取指定开始和结束之间的值，可以指定间隔
# print(random.randrange(1,10))
print(random.randrange(1,7,2)) # 在1,3,5,7之间随机
# choice() 随机获取列表中的值
print(random.choice([1,1,3,4,10]))
# shuffle() 随机打乱列表
# uniform()  随机获取范围内的值(包括小数)
print(random.uniform(1,10))


