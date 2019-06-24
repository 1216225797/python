'''
贪吃蛇游戏：

消息队列Queue：
    消息队列默认Queue.Queue(maxsize)，FIFO(即First In First Out，先进先出)模式；
    默认开启阻塞(block=True)，即队列消息满时，不在接收新的消息，当队列消耗空时，才会重新存放；
    maxsize表示队列最大存放消息数，小于或等于0时表示无限制；
    一般在消息并发量较大的情况下使用，此处是为了降低类与类之间代码的耦合度。

1.蛇(snake类)：
    a.定义蛇的每条线的坐标
    b.蛇移动的算法：
      每移动一次，尾部的坐标删除，头部的坐标增加10px
      向上移动，x轴不变,y轴减小；向下移动，x轴不变，y轴增大；
      向左移动，x轴减小，y轴不变；向右移动，x轴增大，y轴不变；
      canvas.coords(item, 坐标)：移动线或者矩形到指定位置
    c.当蛇头的坐标和食物的坐标重合时，加分并生成新的食物，并增加蛇的长度10
    d.当蛇撞墙，或者和自身坐标重合时，游戏结束。

2.食物(food类)：
    a.随机出现位置，注意出现的范围要略小于画布的大小(因为当食物出现在画布边缘位置时没有游戏体验)
    b.生成新的食物

3.画布(platform类)
    a.创建蛇(create_line)、食物(矩形：create_create_rectangle)、计分板(create_text)
    b.计分板修改文本的方式：canvas.itemconfigure
    c.当游戏结束时，弹出game_over，并弹出按钮“退出”和“继续”
'''
import tkinter as tt
import random
from queue import *
import threading
import time

# 蛇吃到食物的次数
eat_count = 1
class Snake(threading.Thread):
    def __init__(self,queue,platform):
        threading.Thread.__init__(self)
        self.queue = queue
        self.platform = platform
        self.food = Food(self.queue)
        self.score = 0
        self.arrowkey = "Left"
        self.snake_points = [(550,30),(560,30),(570,30),(580,30)]
        # 启动多线程
        self.start()

    def run(self):
        while True:
            if not self.platform.is_game_over:
                # 控制速度
                time.sleep(0.3)
                self.move()

        # th = threading.Thread(target=self.move, args=())
        # 设置为守护线程，主线程结束，子线程也无条件结束
        # th.setDaemon(True)
        # th.start()

    def dir_move(self):
        # 多个值赋值给一个变量，则该变量默认为tuble类型
        self.head_x,self.head_y = self.snake_points[0]
        # print(self.arrowkey)
        if self.arrowkey == "Up":
            self.head_pos = self.head_x, self.head_y - eat_count*10
        elif self.arrowkey == "Down":
            self.head_pos = self.head_x, self.head_y + eat_count*10
        elif self.arrowkey == "Left":
            self.head_pos = self.head_x - eat_count*10, self.head_y
        elif self.arrowkey == "Right":
            self.head_pos = self.head_x + eat_count*10, self.head_y
        return self.head_pos

    def move(self):
        # print("4444")
        new_head_pos = self.dir_move()
        '''
        注意这里的逻辑：
        先弹出最后的坐标，再检查蛇头的坐标是否跟自身重叠(即吃到自己)或者撞墙
        然后再插入新的蛇头
        '''
        # 弹出最后一组坐标
        self.snake_points.pop(-1)
        self.game_over(new_head_pos)
        # 在头部增加新的坐标
        # 这里注意：append是从列表末尾arrowkey追加，所以这里使用insert(Position, value)
        # posititon:表示列表的下标，即从哪插入；value代表插入的值
        self.snake_points.insert(0, new_head_pos)
        self.queue.put({"move":self.snake_points})
        # print(self.snake_points)
        # print("蛇头坐标：",new_head_pos)
        if self.food.pos == new_head_pos:
            print("我们碰面了")
            global eat_count
            eat_count += 1
            self.score += 100
            # 往消息队列添加加分时
            self.queue.put({"add_points":self.score})
            # 吃到食物时增加长度
            # eat_head_pos = self.dir_move()
            # self.snake_points.pop(-1)
            # self.game_over(eat_head_pos)
            # self.snake_points.insert(0, self.eat_head_pos)
            print("吃完食物之后蛇的坐标",self.snake_points)
            # self.queue.put({"add_length":self.snake_points})

            self.food.__init__(self.queue)

    # 获取事件名称
    def get_event_name(self, e):
        self.arrowkey = e.keysym

    # def add_length(self):
    #     if self.arrowkey == "Up":
    #         self.eat_head_pos = self.head_x, self.head_y - eat_count*10
    #     elif self.arrowkey == "Down":
    #         self.eat_head_pos = self.head_x, self.head_y + eat_count*10
    #     elif self.arrowkey == "Left":
    #         self.eat_head_pos = self.head_x - eat_count*10, self.head_y
    #     elif self.arrowkey == "Right":
    #         self.eat_head_pos = self.head_x + eat_count*10, self.head_y
    #     return self.eat_head_pos

    def game_over(self, new_head_pos):
        x,y = new_head_pos[0],new_head_pos[1]
        if not 5 < x < 695 or not 5 < y < 395 or new_head_pos in self.snake_points:
            self.queue.put({"game_over":True})
            # print("我触发了")



class Food():
    def __init__(self,queue):
        self.queue = queue

        # 此处只生成两个坐标是为了和蛇头相遇时做比较
        x = random.randrange(50,600,10)
        y = random.randrange(30,350,10)
        self.pos = x,y
        # 画矩形需要用到的四个值
        self.position = x-20, y-20, x + 20, y + 20
        print("食物坐标：",self.pos)
        # 以字典的形式把食物的坐标放进队列中
        self.queue.put({"food": self.position})


class Platform():
    def __init__(self,queue):
        self.queue = queue
        self.is_game_over = False
        self.root = tt.Tk()
        self.cvs = tt.Canvas(self.root, width= 1000, height=700)
        self.cvs.pack()

        # 初始化蛇
        self.snake_s = self.cvs.create_line((0,0),(0,0), fill="black", width=15)
        # 初始化食物
        self.food_s = self.cvs.create_rectangle(0,0,0,0, fill="black")
        # 初始化计分板
        self.score_s = self.cvs.create_text(650, 20, fill="black", text="分数：0")

        # 使用多线程从消息队列取数据
        t = threading.Thread(target=self.main, args=())
        t.setDaemon(True)
        t.start()


    def myquit(self):
        self.root.quit()

    def gameover(self):
        self.is_game_over = True
        self.cvs.create_text(100, 100, fill="red",text="You Losed!")
        tt.Button(self.root, text="退出", command=self.myquit)
        tt.Button(self.root, text="再来一次", command=self.__init__)

    def main(self):
        try:
            while True:
                    # print("这里是while循环............")
                    # print("88888")
                    # 这里表示从队列里获取到的字典
                    evn = self.queue.get(block=False)
                    # print(self.queue.empty())
                    # 这里表示从字典中获取到的键
                    # 移动
                    if evn.get("move"):
                        # print("这里是move")
                        point_list = list()
                        # 蛇的坐标是以列表形式存到队列中的
                        for snake_point in evn["move"]:
                            for point in snake_point:
                                point_list.append(point)

                        # 移动之后重新画蛇
                        self.cvs.coords(self.snake_s, *point_list)


                        # 生成食物
                    if evn.get("food"):
                        # print("我拿到食物了...")
                        self.cvs.coords(self.food_s, *evn["food"])

                    # 增加长度
                    # if evn.get("add_length"):
                    #     print("增加长度")
                    #     new_point_list = list()
                    #     for snake_point in evn["add_length"]:
                    #         for point in snake_point:
                    #             new_point_list.append(point)
                    #
                    #     self.cvs.coords(self.snake_s, *new_point_list)

                    # 增加积分
                    if evn.get("add_points"):
                        print("增加积分")
                        self.cvs.itemconfigure(self.score_s, text="分数：{0}".format(evn["add_points"]))

                    self.queue.task_done()

                    # 游戏结束
                    if evn.get("game_over"):
                        # print("这里是gameover")
                        self.gameover()
        except Empty:
            if not self.is_game_over:
                self.cvs.after(200, self.main)
        # print("我出不去了")


if __name__ == '__main__':
    queue = Queue()
    platform = Platform(queue)
    snake = Snake(queue,platform)

    platform.root.bind("<Key-Up>", snake.get_event_name)
    platform.root.bind("<Key-Down>", snake.get_event_name)
    platform.root.bind("<Key-Left>", snake.get_event_name)
    platform.root.bind("<Key-Right>", snake.get_event_name)

    platform.root.mainloop()

    # t = threading.Thread(target=platform.main, args=())
    # t.setDaemon(True)
    # t.start()









