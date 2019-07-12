'''
    大飞机类
'''
import tkinter
from airplanewar import AirplaneWar
from readconfig import myconfig

class BigPlane(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height):
        super().__init__(canvas,x,y,position,tag,width,height)
        # super().set_dir([self.conf.getint("bullet", "en_x_dir"),
        #                  self.conf.getint("bullet", "en_y_dir")])
        self.speed = [myconfig.bp_x_step,myconfig.bp_y_step]
        self.dir = [myconfig.bp_x_dir,myconfig.bp_y_dir]
        # 实例化图片
        for i in range(5):
            img_path = myconfig.bp_img_path+str(i) + myconfig.bp_img_suffix
            self.bigplane_img = tkinter.PhotoImage(file=img_path)
            self.img_list.append(self.bigplane_img)


    def move(self):
        x = self.speed[0] * self.dir[0]
        y = self.speed[1] * self.dir[1]
        self.enemy_move(self.tag, x, y)

