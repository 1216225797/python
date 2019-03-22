# 随机数比较
# 输入一个三位数，如果输入的数字比随机数大，则分别打印该数的个，十，百位
# 如果输入的数字比三位数小，则输出一串120位的随机字符串到文本(规则：每行打印12个字符，且前四位是字母，后八位是数字)
# 如果等于随机数，则打印“You Win！”


# 该题目用到的知识点：
# 1.随机数(需要先import random模块)
# 2.chr()函数和ord()函数及ascii对应关系
# 3.信息输出到文本文件:
#   语法：
#        with open('文件名','输入格式，例如:w 写入，a 追加写入')  as 名称(可以随便取):
#                名称.write(文本信息)


import random

class GameNum():
    def print_str(self):
        str_num = ''

        for m in range(4):
            zm = random.randrange(65, 90)

            # chr函数是将数字通过ascii值转化为对应的字母
            # ord函数是将字母通过ascii值转化为对应的数字
            zm1 = chr(zm)

            str_num = str_num + zm1

        for n in range(8):
            sz = random.randrange(0, 10)

            str_num = str_num + str(sz)

        # 这里记得要返回值，否则下面调用函数的时候得不到结果
        return str_num


    def game(self):
    # randint 和 randrange都包含两个端点
    # randint是随机生成整数
    # randrange可以包含字符
        number = random.randint(100, 999)


        total = 0 # 输入的次数
        right = 0 # 猜对的次数

        while 1:


            num = input("请输入一个三位数字，输入-1退出：")

            if num == '-1':
                break
            # isdigit()函数表示判断一个字符串是否是一个数字
            if num.isdigit() and 100 <= int(num) <= 999:
                if int(num) > number:
                    gw = num[2]
                    sw = num[1]
                    bw = num[0]
                    print("个位：{0},十位：{1},百位：{2}".format(gw,sw,bw))
                elif int(num) == number:
                    print("You Win")
                    right += 1
                else:
                    # 循环调用10次打印一行字符串的函数
                    for i in range(10):
                        s = num.print_str()
                        with open('str_num.txt', 'a') as ff:
                            ff.write(s + '\n')
                # 每输入一次，次数+1，错误输入不计算在内
                total += 1
                # 猜对的概率
                gl = right // total
                print("你输入了{0}次".format(total))
                print("猜中的概率为:{0}".format(gl))


            else:
                print("输入有误，请重新输入")

num = GameNum()