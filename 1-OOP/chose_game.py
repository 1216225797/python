import rand_shuzi
import rand_zimu



print("请选择游戏\n1.数字游戏\n2.字母游戏")
a = input("输入1或2：")
if a == '1':
    # 实例化
   num =  rand_shuzi.GameNum
   # 0代表self参数
   num.game(0)
elif a == '2':
    zimu = rand_zimu.GameZimu
    b = input("请输入A-D其中一个大写字母：")
    zh = ord(b)

    if zh == 65:
        zimu.a()
    elif zh == 66:
        zimu.b()
    elif zh == 67:
        zimu.c()
    elif zh == 68:
        zimu.d()
    else:
        print("请按规则输入！")
else:
    print("请按规则输入！")
