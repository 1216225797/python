'''
计算器：
    项目分析：
        1.画界面，布局等
            a.同一个父组件中有了grid()，就不能有pack()，会报错
        2.编写每个按钮实现功能的方法
'''

import tkinter as t


class Calculation():
    def __init__(self):

        # 第一个数字
        self.num1 = ''
        # 第二个数字
        self.num2 = ''
        # 运算符
        self.operator = ''
        # 是否按下等号
        # self.es = False

    def del_num(self):
        if self.operator == "=":
            print("我是等号")
            return None
        else:
            if self.operator:
                self.num2 = self.num2[:-1]
                sv.set(self.num1 + self.operator +self.num2)
                print(self.operator)
                print("num2被删除了")
            else:
                self.num1 = self.num1[:-1]
                sv.set(self.num1)
                print("num1被删除了")

    def reset_num(self):
        # self.num1 = ''
        self.__init__()
        sv.set("0")

        print("我重置了...")

    '''
    1.如果是第一个操作数则直接显示
    2.如果是第二个操作数，则显示第一个操作数、运算符和第二个操作数
    3.判断是第一个还是第二个操作数，可以根据是否按下运算符判断
    '''
    def oper(self,opt):
        if opt in ["+","-","*","/"]:
            self.operator= opt
            sv.set(self.num1 + self.operator)
        else:# 否则按的是等号
            # 判断按下的是否是等号，如果是则计算值
            if self.operator == "+":
                res = int(self.num1) + int(self.num2)
            if self.operator == "-":
                res = int(self.num1) - int(self.num2)
            if self.operator == "*":
                res = int(self.num1) * int(self.num2)
            if self.operator == "/":
                res = int(self.num1) / int(self.num2)
            self.operator = opt
            sv.set(res)


    def splice_num(self,num):
        # 如果operator不是"+","-","*","/"，则说明操作的是第二个数
        if self.operator in ["+","-","*","/"]:
            self.num2 += num
            print(self.operator)
            sv.set(self.num1 + self.operator + self.num2)
        # 如果运算符是等号，则代表上一轮计算完成，下一轮开始
        elif self.operator == "=":
            self.__init__()
            self.num1 += num
            sv.set(self.num1)
        # 否则按下的是第一个数
        else:
            self.num1 += num
            sv.set(self.num1)






if __name__ == '__main__':
    cal = Calculation()

    root = t.Tk()
    # 设置窗口大小
    root.title("我的计算器")
    root.geometry("300x350")
    # 固定窗口(参数代表允许调整的大小)
    root.resizable(0, 0)
    # ------------------------定义顶部区域----------------------------------------------------------------
    # 定义Frame面板
    f1 = t.Frame(root, background="#dddddd")
    # print(self.f1)
    f1.pack()
    # 只有添加了下面这句话，Frame设置宽高才有用
    # self.f1.pack_propagate(0)

    # 设置文本框显示的值，配合textvariable使用
    sv = t.StringVar()
    sv.set("0")
    # anchor:锚点，控制文本在控件上的显示位置，e代表东部
    # justify:多行文本时的对齐方式
    # padx:x的方向的外边距；pady:y方向的外边距
    lb = t.Label(f1, textvariable=sv, width=17, height=1,
                      background="white", font=("黑体", 20, "bold"),
                      justify=t.RIGHT, anchor='e')
    # print(self.lb)
    lb.grid(padx=10, pady=10)
    # ------------------------定义按键区域----------------------------------------------------------------------
    f2 = t.Frame(root, width=280, height=250)
    f2.pack()
    # 只有添加了下面这句话，Frame设置宽高才有用
    f2.pack_propagate(0)
    bt1 = t.Button(f2, width=4, height=1, text="←", bg="#dddddd", font=("黑体", 10, "bold"),
                        command=cal.del_num)
    bt1.grid(padx=10, pady=10)
    bt2 = t.Button(f2, width=4, height=1, text="C", bg="#dddddd", font=("黑体", 10, "bold"),
                        command=cal.reset_num)
    bt2.grid(pady=10, row=0, column=1)
    bt3 = t.Button(f2, width=4, height=1, text="±", bg="#dddddd", font=("黑体", 10, "bold"))
    bt3.grid(padx=10, pady=10, row=0, column=2)
    bt4 = t.Button(f2, width=4, height=1, text="√", bg="#dddddd", font=("黑体", 10, "bold"))
    bt4.grid(pady=10, row=0, column=3)

    # 用到lambda函数是因为command参数要参数函数本身(即函数后不带括号),但函数又要传递参数
    bt5 = t.Button(f2, width=4, height=1, text="7", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("7"))
    bt5.grid(padx=10, pady=10, row=1, column=0)
    bt6 = t.Button(f2, width=4, height=1, text="8", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("8"))
    bt6.grid(pady=10, row=1, column=1)
    bt7 = t.Button(f2, width=4, height=1, text="9", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("9"))
    bt7.grid(padx=10, pady=10, row=1, column=2)
    bt8 = t.Button(f2, width=4, height=1, text="4", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("4"))
    bt8.grid(pady=10, row=2, column=0)
    bt9 = t.Button(f2, width=4, height=1, text="5", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("5"))
    bt9.grid(padx=10, pady=10, row=2, column=1)
    bt10 = t.Button(f2, width=4, height=1, text="6", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("6"))
    bt10.grid(pady=10, row=2, column=2)
    bt11 = t.Button(f2, width=4, height=1, text="1", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("1"))
    bt11.grid(padx=10, pady=10, row=3, column=0)
    bt12 = t.Button(f2, width=4, height=1, text="2", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("2"))
    bt12.grid(pady=10, row=3, column=1)
    bt13 = t.Button(f2, width=4, height=1, text="3", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("3"))
    bt13.grid(padx=10, pady=10, row=3, column=2)
    bt14 = t.Button(f2, width=6, height=1, text="0", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda:cal.splice_num("0"))
    bt14.grid(pady=10, row=4, column=0)
    bt15 = t.Button(f2, width=4, height=1, text="/", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda :cal.oper("/"))
    bt15.grid(padx=10, pady=10, row=1, column=3)
    bt16 = t.Button(f2, width=4, height=1, text="*", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda :cal.oper("*"))
    bt16.grid(pady=10, row=2, column=3)
    bt17 = t.Button(f2, width=4, height=1, text="-", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda :cal.oper("-"))
    bt17.grid(padx=10, pady=10, row=3, column=3)
    bt18 = t.Button(f2, width=4, height=1, text="+", bg="#dddddd", font=("黑体", 10, "bold"),command=lambda :cal.oper("+"))
    bt18.grid(pady=10, row=4, column=3)
    bt19 = t.Button(f2, width=6, height=1, text="=", bg="#dddddd", font=("黑体", 10, "bold"), command=lambda :cal.oper("="))
    bt19.grid(padx=10, pady=10, row=4, column=1)

    root.mainloop()

