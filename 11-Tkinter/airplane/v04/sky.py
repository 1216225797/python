'''
    背景图片类
'''
from configparser import ConfigParser
import tkinter
from airplanewar import AirplaneWar

class Sky(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height):
        super(Sky,self).__init__(canvas,x,y,position,tag,width,height)

        # 创建背景图片
        self.bg_path = self.conf.get("background", "path")
        self.bg = tkinter.PhotoImage(file=self.bg_path)

        # 移动速度
        self.speed = (self.conf.getint("background","x_step"),self.conf.getint("background","y_step"))
        # 移动方向
        self.move_dir = (self.conf.getint("background","x_dir"),self.conf.getint("background","y_dir"))


    def move(self):
        x = self.speed[0] * self.move_dir[0]
        y = self.speed[1] * self.move_dir[1]
        self.enemy_move(self.tag,x,y)

