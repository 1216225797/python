# 写一个6位随机验证码程序，要求验证码中至少包含一个数字，一个小写字母，一个大写字母
import random
import string

code = []
# 保证至少有一个数字
code.append(random.choice(string.digits))
# 保证至少有一个大写字母
code.append(random.choice(string.ascii_uppercase))
# 保证至少一个小写字母
code.append(random.choice(string.ascii_lowercase))

while len(code) < 6:
    code.append(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase))
# print(code)

'''
语法：  'sep'.join(seq)

参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
'''
new_code = ''.join(code)
print(new_code)