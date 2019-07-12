'''
    小飞机飞机类
'''
import tkinter
from airplanewar import AirplaneWar
from readconfig import myconfig

class SmallPlane(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height):
        super().__init__(canvas,x,y,position,tag,width,height)
        self.speed = [myconfig.sp_x_step,myconfig.sp_y_step]
        self.dir = [myconfig.sp_x_dir,myconfig.sp_y_dir]
        # 实例化图片
        for i in range(5):
            img_path = myconfig.sp_img_path+str(i) + myconfig.sp_img_suffix
            self.smallplane_img = tkinter.PhotoImage(file=img_path)
            self.img_list.append(self.smallplane_img)


    def move(self):
        x = self.speed[0] * self.dir[0]
        y = self.speed[1] * self.dir[1]
        self.enemy_move(self.tag, x, y)

