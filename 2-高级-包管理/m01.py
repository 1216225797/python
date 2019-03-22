import random

while(1):
    s = input("请输入一个0~999的数字:")
    if s.isdigit() and 0 <= int(s) <= 999:
        if int(s) > random.randint(0,999):
            print("你输入的数字比随机数大！")

        if int(s) < random.randint(0,999):
            print("你输入的数字比随机数小！")

        if int(s) == random.randint(0,999):
            print("你中奖了！")
            break

    else:
        print("输入有误！请重新输入！")