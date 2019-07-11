'''
    英雄机类
'''
from airplanewar import AirplaneWar
import tkinter
from configparser import ConfigParser

class Hero(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height,window):
        super().__init__(canvas,x,y,position,tag,width,height)
        super().set_health(self.conf.getint("game","hero_health"))
        # 图片实例
        # r_path = self.conf.get("hero","img_path")
        # self.r_hero_img = tkinter.PhotoImage(file = r_path)
        for i in range(5):
            img_path = self.conf.get("hero","img_path_"+str(i))
            self.hero_img = tkinter.PhotoImage(file = img_path)
            self.img_list.append(self.hero_img)
        # 移动步长
        self.speed = [self.conf.getint("hero","x_speed"),self.conf.getint("hero","y_speed")]
        # 移动方向
        self.dir = [0,-1]

        # 事件绑定
        window.bind("<Key-Up>", self.hero_move)
        window.bind("<Key-Down>", self.hero_move)
        window.bind("<Key-Left>", self.hero_move)
        window.bind("<Key-Right>", self.hero_move)


    def move(self):
        # 窗口边界
        canvas_width = self.conf.getint("interface","canvas_width")
        canvas_height = self.conf.getint("interface","canvas_height")



        # 窗口边界之内执行移动
        if self.nw_pos[0] >=0 and self.se_pos[0] <= canvas_width \
        and self.nw_pos[1] >= 0 and self.se_pos[1] <= canvas_height:
            # 默认向上
            x = self.speed[0] * self.dir[0]
            y = self.speed[1] * self.dir[1]
            self.enemy_move(self.tag,x,y)
        else:
            if self.nw_pos[0] < 0:
                self.enemy_move(self.tag,-self.nw_pos[0],0)
            elif self.ne_pos[0] > canvas_width:
                self.enemy_move(self.tag, -(self.se_pos[0] - canvas_width),0)
            elif self.nw_pos[1] < 0:
                self.enemy_move(self.tag, 0, -self.nw_pos[1] )
            elif self.se_pos[1] > canvas_height:
                self.enemy_move(self.tag, 0, -(self.se_pos[1] - canvas_height))


    def hero_move(self,e):
        if e.keysym == "Up":
            self.dir = [0,-1]
            self.move()
        if e.keysym == "Down":
            self.dir = [0,1]
            self.move()
        if e.keysym == "Left":
            self.dir = [-1,0]
            self.move()
        if e.keysym == "Right":
            self.dir = [1,0]
            self.move()

    # 重置英雄机
    def reset_pos(self):
        x = self.anchor_x - self.center_pos[0]
        y = self.anchor_y - self.center_pos[1]
        self.enemy_move(self.tag, x, y)
        # for i in range(5):
        #         #     path = self.conf.get("hero", "img_path_" + str(i))
        #         #     reset_hero_img = tkinter.PhotoImage(file=path)
        #         #     self.img_list.append(reset_hero_img)
        #         # self.canvas.create_image(self.anchor_x,
        #         #                          self.anchor_y,
        #         #                          image=self.hero_img[0],
        #         #                          anchor=self.anchor,
        #         #                          tags=self.tag)
        # 更新坐标值
        # self.update_pos(x, y)
        # self.state = self.conf.getint("game", "status_alive")


