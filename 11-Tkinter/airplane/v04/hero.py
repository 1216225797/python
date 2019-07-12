'''
    英雄机类
'''
from airplanewar import AirplaneWar
from readconfig import myconfig
import tkinter

class Hero(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height,window):
        super().__init__(canvas,x,y,position,tag,width,height)
        super().set_health(myconfig.hero_health)
        # 图片实例
        # r_path = self.conf.get("hero","img_path")
        # self.r_hero_img = tkinter.PhotoImage(file = r_path)
        for i in range(5):
            img_path = myconfig.hero_img_path+str(i) + myconfig.hero_img_suffix
            self.hero_img = tkinter.PhotoImage(file = img_path)
            self.img_list.append(self.hero_img)
        # 移动步长
        self.speed = [myconfig.hero_x_step,myconfig.hero_y_step]
        # 移动方向
        self.dir = [0,-1]

        # 事件绑定
        window.bind("<Key-Up>", self.hero_move)
        window.bind("<Key-Down>", self.hero_move)
        window.bind("<Key-Left>", self.hero_move)
        window.bind("<Key-Right>", self.hero_move)


    def move(self):
        # 窗口边界
        canvas_width = myconfig.cvs_w
        canvas_height = myconfig.cvs_h



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
        x = 0
        y = 0
        if self.anchor == "center":
            x = self.anchor_x - self.center_pos[0]
            y = self.anchor_y - self.center_pos[1]
        elif self.anchor == "nw":
            x = self.anchor_x - self.nw_pos[0]
            y = self.anchor_y - self.ne_pos[1]
        elif self.anchor == "ne":
            x = self.anchor_x - self.ne_pos[0]
            y = self.anchor_y - self.ne_pos[1]
        elif self.anchor == "se":
            x = self.anchor_x - self.se_pos[0]
            y = self.anchor_y - self.se_pos[1]
        elif self.anchor == "sw":
            x = self.anchor_x - self.sw_pos[0]
            y = self.anchor_y - self.sw_pos[1]
        self.enemy_move(self.tag, x, y)


