'''
    背景图片类
'''

import tkinter
from airplanewar import AirplaneWar
from readconfig import myconfig

class Sky(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height):
        super(Sky,self).__init__(canvas,x,y,position,tag,width,height)

        # 创建背景图片
        self.bg_path = myconfig.bg_img_path
        self.bg = tkinter.PhotoImage(file=self.bg_path)

        # 移动速度
        self.speed = [myconfig.bg_x_step,myconfig.bg_y_step]
        # 移动方向
        self.move_dir = [myconfig.bg_x_dir,myconfig.bg_y_dir]


    def move(self):
        x = self.speed[0] * self.move_dir[0]
        y = self.speed[1] * self.move_dir[1]
        self.enemy_move(self.tag,x,y)

