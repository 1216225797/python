'''
    小蜜蜂类
'''
from airplanewar import AirplaneWar
from readconfig import myconfig
import random
import tkinter


class Bee(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height,x_dir,cvs_w):
        super(Bee,self).__init__(canvas,x,y,position,tag,width,height)
        # 移动速度
        self.speed = [myconfig.bee_x_step,myconfig.bee_y_step]
        # 初始x轴移动方向随机，y轴一直向下
        self.x_dir = x_dir
        self.cvs_w = cvs_w

        for i in range(5):
            img_path = myconfig.bee_img_path + str(i) + myconfig.bee_img_suffix
            self.bee_img = tkinter.PhotoImage(file = img_path)
            self.img_list.append(self.bee_img)


    def move(self):
        # 当碰到窗口边缘时反弹
        if self.nw_pos[0] < 0 or self.ne_pos[0] > self.cvs_w:
            self.x_dir = -self.x_dir

        self.enemy_move(self.tag, self.speed[0] * self.x_dir, self.speed[1])

