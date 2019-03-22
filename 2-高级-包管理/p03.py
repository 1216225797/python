'''

用户登录程序
{"expire_date":"2021-01-01"."id":"1234","status":0,"pay_day":22,"password":"abc"}

1.用户名为1234.json
2.判断是否过期，与expire_date做比较
3.登录成功后打印登录成功，三次登录失败status修改为1，并且锁定账号

'''
from datetime import datetime
s = datetime.now().strftime("%Y-%m-%d")
print(s)

username = input("请输入账号：")
if username == '1234.json' :
    password = input("请输入密码：")
# elif:
#     pass
