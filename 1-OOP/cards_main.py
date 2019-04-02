'''
名片管理系统

1. 需求
    1.1 程序启动，显示名片管理系统欢迎页面，并显示功能菜单
    1.2 用户用数字显示不同的功能
    1.3 根据功能选择，执行不同的功能
    1.4 用户名片需要记录用户的姓名、电话、QQ、邮件
    1.5 如果查询到指定的名片，用户可以选择修改或者删除名片
2. 文件准备
    2.1 新建cards_main.py保存主程序功能代码
        2.1.1 程序的入口
        2.1.2 每一次启动名片管理系统都通过main这个文件启动
    2.2 新建cards_tools.py保存所有名片功能函数
        2.2.1 将对名片的新增、查询、修改、删除等功能封装在不同的函数中
'''

import cards_tools

while True:

    cards_tools.cards_main()

    input_num = input("请选择功能：")
    if input_num == "1":
        cards_tools.cards_insert()
    elif input_num == "2":
        cards_tools.show_all()
    elif input_num == "3":
        cards_tools.cards_select()
    elif input_num == "0":
        print("期待您再次使用！")
        break
    else:
        print("请按规定输入！")