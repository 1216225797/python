'''
面向对象案例
'''

import random


number = random.randint(100, 999)




num = input("请输入一个三位数字：")
if num.isdigit() and 100 <= int(num) <= 999:
        if int(num) > number:
            print(num[0],',',num[1],',',num[2])
        elif int(num) == number:
            print("You Win")
        else:
            print("太小了")
else:
        print("输入有误，请重新输入")




