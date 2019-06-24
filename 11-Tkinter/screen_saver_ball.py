'''
屏保项目：

1.定义球类：
    a.球的初始位置、大小、数量、颜色、移动速度都随机
    b.tkinter中只有画椭圆的方法：create_oval，即在长方形内画出；
      圆形是特殊的一种椭圆(正方形内)
    c.只需要得到正方形左上角和右下角的坐标，就可以画出一个园；根据初始位置
      圆心的坐标可以得出
    d.当撞到屏幕边缘时，往反方向移动

2.定义屏保类
    a.需要得到屏幕的长和宽
    b.当鼠标和键盘有任何事件时取消屏保

'''
import random as r
import tkinter as t

# 声明全局变量用来计算鼠标移动或者键盘点击时产生事件调用函数的次数
i = 0
class ScreenSaver():
    def __init__(self):
        # 每次启动屏保时球的数量随机
        self.balls = r.randint(5,10)

        self.base = t.Tk()

        # 取消边框
        self.base.overrideredirect(1)

        # 获取屏幕的宽度
        self.screen_w = self.base.winfo_screenwidth()
        # 获取屏幕高度
        self.screen_h = self.base.winfo_screenheight()

        # 当鼠标点击时，退出屏保
        self.base.bind('<Motion>', self.quit_ss)
        # 当任意键盘点击，退出屏保
        self.base.bind('<Key>', self.quit_ss)

        self.cvs = t.Canvas(self.base, width=self.screen_w, height=self.screen_h)
        self.cvs.grid()

        self.start_balls()
        self.run_balls()


        self.base.mainloop()


    # 声明list用来存放多个球
    balls_list = []
    # 生成多个球
    def start_balls(self):
        for i in range(self.balls):
            ssb = RandomBall(self.screen_w, self.screen_h)
            ssb.create_ball(self.cvs)
            self.balls_list.append(ssb)

    # 让球一直移动
    def run_balls(self):
        for ball_s in self.balls_list:
            ball_s.move_ball()
        # 这句话的意思是多少毫秒后启动一个函数
        self.cvs.after(200, self.run_balls)


    def quit_ss(self,e):
        global i
        i += 1
        # 只弹出一次按钮，后面再有事件不执行该函数
        if i<= 1:
            b = t.Button(self.base, text=e, command=self.button_event)
            b.grid(row=0, column=0)


        # print("哈哈，我被调用了....")

    def button_event(self):
        self.base.quit()



class RandomBall():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # 定义球初始位置的x坐标
        self.initial_x = r.randint(self.screen_width-700, self.screen_width-200)
        # 定义球初始位置的y坐标
        self.initial_y = r.randint(self.screen_height-300, self.screen_height-100)

        # 定义球的半径
        self.radius = r.randint(40,100)

        # 定义球的每次移动的距离(速度)
        self.moved_x = r.randint(5,20)
        self.moved_y = r.randint(5,20)

        # 定义球的颜色
        x = lambda: r.randint(0,255)
        # %02x占位符表示：十六进制字符，不足两位以0补充
        self.ball_color = '#%02x%02x%02x'%(x(), x(), x())

        # 左上角x坐标,初始位置圆心x坐标减去半径，其他同理
        self.upper_left_x = self.initial_x - self.radius
        # 左上角y坐标
        self.upper_left_y = self.initial_y + self.radius
        # 右下角x坐标
        self.lower_right_x = self.initial_x + self.radius
        # 右下角y坐标
        self.lower_right_y = self.initial_y - self.radius

    def create_ball(self, canvas):
        self.cvs = canvas
        self.ball =  self.cvs.create_oval(self.upper_left_x, self.upper_left_y, self.lower_right_x, self.lower_right_y, fill=self.ball_color, outline=self.ball_color)
    # 注意：这里只移动了一次
    def move_ball(self):
        self.initial_x += self.moved_x
        self.initial_y += self.moved_y
        # self.lower_right_x += self.moved_x
        # self.lower_right_y += self.moved_y
        # 当碰到左壁时
        # 算法：当前左上角坐标加上移动距离大于等于屏幕的宽度
        if self.initial_x - self.radius <= 0:
            # print(self.initial_x + self.radius)
            self.moved_x = -self.moved_x
        # 当碰到右壁时
        if self.initial_x + self.radius >= self.screen_width:
            # print(self.lower_right_x)
            self.moved_x = -self.moved_x
        # 当碰到底时
        if self.initial_y - self.radius <= 0:
            # print(self.initial_y + self.radius)
            self.moved_y = -self.moved_y
        # 当碰到上沿时
        if self.initial_y + self.radius >= self.screen_height:
            # print(self.lower_right_y)
            self.moved_y = -self.moved_y

        self.cvs.move(self.ball, self.moved_x, self.moved_y)


if __name__ == '__main__':
    screen_saver = ScreenSaver()