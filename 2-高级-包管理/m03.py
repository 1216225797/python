'''

用户登录程序，文件如下1234.json
{"expire_date":"2021-01-01"."id":"1234","status":0,"pay_day":22,"password":"abc"}

1.用户名为json的文件名
2.判断是否过期，与expire_date做比较
3.登录成功后打印登录成功，三次登录失败status修改为1，并且锁定账号

所用到的知识点:
1. open()函数，打开或新建一个文件
    语法：open(name, mode , buffering)
        name:文件名
        mode:打开文件的模式：只读，写入，追加等。这个参数是非强制的，默认文件访问模式为只读(r)，
             更多权限参考360浏览器收藏文章“Python open()函数”
            r+：打开一个文件用于读写。文件指针将会放在文件的开头。
        buffering：buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。
                   如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

2. str.strip()函数，去掉字符串中的空格

3. file.seek()函数,用于移动文件读取指针到指定位置
    语法：file.seek(offset, whence)
        offset: 开始的偏移量，也就是代表需要移动偏移的字节数
        whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
                0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起

4. file.truncate()函数，用于截断文件并返回截断的字节长度
    语法：file.truncate(size)
         size可选
        指定长度的话，就从文件的开头开始截断指定长度，其余内容删除；
        不指定长度的话，就从文件开头开始截断到当前位置，其余内容删除。
5. json.dumps()和json.loads()是json格式处理函数（可以这么理解，json是字符串）
　　 (1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　 (2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

   json.dump()和json.load()主要用来读写json文件函数

'''
import json
import os.path as op
from datetime import datetime


# s = datetime.now().strftime("%Y-%m-%d")
# print(s)

# # msg = {"expire_date":"2021-01-01","id":"1234","status":0,"pay_day":22,"password":"abc"}
# expire_time = msg["expire_date"]
# # print(expire_time)
# passwd = msg["password"]
# # print(passwd)

i = 3
# 这里定义一个变量用来记录是否登录成功，如果成功则退出整个循环
is_success = False


while i > 0:
    username = input("请输入账号：\n")
    # 拼接输入账号的文件名，并去除空格
    f = username.strip() + '.json'
    # 如果文件名称和已知的文件匹配，即账号正确，则读取该文件内容
    if op.exists(f):
        fp = open(f, "r+", encoding="utf-8")
        # 读取文件内容，把字符串格式的信息转化为字典类型的信息
        user_msg = json.load(fp)
        print(user_msg)
        print(type(user_msg))
        if user_msg["status"] == 1:
            print("账号已被锁定")
            break
        else:
            curr_date = datetime.now().strftime("%Y-%m-%d")
            exp_date = user_msg["expire_date"]
            if curr_date > exp_date:
                print("账号已过期！")
            else:
                while i > 0:
                    passwd = input("请输入密码：\n")
                    if passwd == user_msg["password"]:
                        print("登录成功")
                        # 登录成功则把该值修改为True
                        is_success = True
                        break
                    else:
                        print("密码输入有误！")
                        if i == 1:
                            print("用户登录超过3次，锁定账号！")
                            # 移动文件指针到开始位置
                            fp.seek(0)
                            # 清空文件内容
                            fp.truncate()
                            user_msg["status"] = 1
                            # 要先清空文件再写入，不然会在文件末尾追加写入生成重复数据
                            json.dump(user_msg,fp)
                        i -= 1
    else:
        print("用户不存在！")
        i -= 1

    # if后面跟的条件必为True
    if is_success:
        break