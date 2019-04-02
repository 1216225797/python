'''
实现名片新增，删除，修改，查询功能

'''
# 申明一个列表存放名片字典
cards_list = []

def cards_main():
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0 \n")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片\n")
    print("0. 退出系统")
    print("*" * 50)

# 新增
def cards_insert():
    cards_dict = {}
    cards_dict["姓名"] = input("姓名：")
    cards_dict["电话"] = input("电话：")
    cards_dict["QQ"] = input("QQ：")
    cards_dict["邮箱"] = input("邮箱：")
    if len(cards_dict["姓名"]) == 0:
        print("姓名不能为空！")
    else:
        cards_list.append(cards_dict)
        print("{0}的名片已新建成功！".format(cards_dict["姓名"]))
    # for k,v in cards_dict.items():
    #     print(k,v)

def cards_del(find_dict):
    cards_list.remove(find_dict)
    print("删除成功！")

def cards_select():

    if len(cards_list) == 0:
        print("当前没有名片哦！亲！")
    else:
        cx_name = input("请输入你要查询的名字：")
        for find_dict in cards_list:
            # print(type(find_dict))
            # print(find_dict)
            if find_dict['姓名'] == cx_name:
                print("=" * 50)
                print("姓名：{0}".format(find_dict["姓名"]))
                print("电话：{0}".format(find_dict["电话"]))
                print("QQ：{0}".format(find_dict["QQ"]))
                print("邮箱：{0}".format(find_dict["邮箱"]))
                print("=" * 50)
                while True:
                    print("a.修改名片   b.删除名片   q.返回上级菜单")
                    s = input("请选择你的操作：\n")
                    if s in ["a", "b","q"]:
                        if s == "a":
                            find_dict["姓名"] = input_message(find_dict["姓名"],"请输入你的姓名：")
                            find_dict["电话"] = input_message(find_dict["电话"],"请输入你的电话：")
                            print("修改成功！")
                            print("=" * 50)
                            print("姓名：{0}".format(find_dict["姓名"]))
                            print("电话：{0}".format(find_dict["电话"]))
                            print("QQ：{0}".format(find_dict["QQ"]))
                            print("邮箱：{0}".format(find_dict["邮箱"]))
                            print("=" * 50)
                        elif s == "b":
                            cards_del(find_dict)
                            break
                        elif s == "q":
                            break
                            cards_main()
                        else:
                            print("请输入有效的选择！")
            else:
                print("名片不存在！")


def show_all():
    if len(cards_list) == 0:
        print("当前没有名片哟！亲！")
    else:
        # 遍历列表
        for i in cards_list:
            print("=" * 50)
            print("姓名：{0}".format(i["姓名"]))
            print("电话：{0}".format(i["电话"]))
            print("QQ：{0}".format(i["QQ"]))
            print("邮箱：{0}".format(i["邮箱"]))
            print("=" * 50)

'''
此函数是用来判断修改名片信息时输入内容是否为空
如果为空，则显示原来信息，不为空则为修改之后的值
cust_msg：原来的信息
input:输入的信息

return的用法:将结果返回到调用的地方，并把程序的控制权一起返回
程序运行到所遇到的第一个return即返回（退出def块），不会再运行第二个return。
(我自己的理解：如果有返回值，即将整个函数当做一个结果返回到调用此函数的地方)

'''
def input_message(cust_msg,input_msg):
    rstr = input(input_msg)
    if len(rstr) == 0:
        return cust_msg
    else:
        return rstr