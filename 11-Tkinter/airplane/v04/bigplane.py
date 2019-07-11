'''
    大飞机类
'''
import tkinter
from airplanewar import AirplaneWar

class BigPlane(AirplaneWar):
    def __init__(self,canvas,x,y,position,tag,width,height):
        super().__init__(canvas,x,y,position,tag,width,height)
        # super().set_dir([self.conf.getint("bullet", "en_x_dir"),
        #                  self.conf.getint("bullet", "en_y_dir")])
        self.speed = [self.conf.getint("bigplane","x_step"),self.conf.getint("bigplane","y_step")]
        self.dir = [self.conf.getint("bigplane","x_dir"),self.conf.getint("bigplane","y_dir")]
        # 实例化图片
        for i in range(5):
            img_path = self.conf.get("bigplane","img_path_"+str(i))
            self.bigplane_img = tkinter.PhotoImage(file=img_path)
            self.img_list.append(self.bigplane_img)


    def move(self):
        x = self.speed[0] * self.dir[0]
        y = self.speed[1] * self.dir[1]
        self.enemy_move(self.tag, x, y)

