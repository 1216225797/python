'''
    飞机大战v04
        用面向对象的方式实现
        此类为所有对象的基类

    参数解释：
        x:锚点x坐标值
        y:锚点y坐标值
        position:锚点位置
        play: 游戏是否进行中
'''
import random
import tkinter
import time
from readconfig import myconfig

class AirplaneWar():
    def __init__(self,canvas,x,y,position,tag,width,height):
        self.canvas = canvas
        # 锚点坐标
        self.anchor_x = x
        self.anchor_y = y
        # 锚点
        self.anchor = position
        # 当前对象的tags
        self.tag = tag
        self.width = width
        self.height = height
        self.play = True
        # 死亡动画图片的下标
        self.img_idx = 0
        # 存放爆炸图片实例的列表
        self.img_list = []
        # self.hero_img_list = []
        # 各个游戏部件的初始状态
        self.state = myconfig.status_alive
        # 默认生命值
        self.health = myconfig.enemy_health
        # 爆炸结束标识
        self.is_explosion = False

        # 各个点的坐标
        self.nw_pos = self.get_nw_pos()
        self.ne_pos = self.get_ne_pos()
        self.se_pos = self.get_se_pos()
        self.sw_pos = self.get_sw_pos()
        self.center_pos = self.get_center_pos()

    # 指定对象移动
    def enemy_move(self,tag,x,y):
        self.canvas.move(tag,x,y)
        self.update_pos(x,y)

    # 更新各个点的坐标值
    def update_pos(self,x,y):
        for i in self.nw_pos,self.ne_pos,self.se_pos,self.sw_pos,self.center_pos:
            i[0] += x
            i[1] += y

    # 获取对象左上角坐标
    # 这里需要注意返回值应为list类型，因为tuple类型只支持读不支持修改值的操作
    def get_nw_pos(self):
        if self.anchor == "nw":
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == "ne":
            return [self.anchor_x - self.width, self.anchor_y]
        elif self.anchor == "sw":
            return [self.anchor_x, self.anchor_y - self.height]
        elif self.anchor == "center":
            return [self.anchor_x - self.width/2, self.anchor_y - self.height/2]
    # 右上角
    def get_ne_pos(self):
        if self.anchor == "nw":
            return [self.anchor_x + self.width, self.anchor_y]
        elif self.anchor == "ne":
            return [self.anchor_x,self.anchor_y]
        elif self.anchor == "se":
            return [self.anchor_x, self.anchor_y - self.height]
        elif self.anchor == "sw":
            return [self.anchor_x + self.width, self.anchor_y - self.height]
        elif self.anchor == "center":
            return [self.anchor_x + self.width/2, self.anchor_y - self.height/2]

    # 右下角
    def get_se_pos(self):
        if self.anchor == "nw":
            return [self.anchor_x + self.width, self.anchor_y + self.height]
        elif self.anchor == "ne":
            return [self.anchor_x,self.anchor_y + self.height]
        elif self.anchor == "se":
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == "sw":
            return [self.anchor_x + self.width, self.anchor_y]
        elif self.anchor == "center":
            return [self.anchor_x + self.width/2, self.anchor_y + self.height/2]

    # 左下角
    def get_sw_pos(self):
        if self.anchor == "nw":
            return [self.anchor_x, self.anchor_y + self.height]
        elif self.anchor == "ne":
            return [self.anchor_x - self.width,self.anchor_y + self.height]
        elif self.anchor == "se":
            return [self.anchor_x + self.width, self.anchor_y]
        elif self.anchor == "sw":
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == "center":
            return [self.anchor_x - self.width/2, self.anchor_y + self.height/2]

    # 中心点
    def get_center_pos(self):
        if self.anchor == "nw":
            return [self.anchor_x - self.width/2, self.anchor_y - self.height/2]
        elif self.anchor == "ne":
            return [self.anchor_x + self.width/2,self.anchor_y - self.height/2]
        elif self.anchor == "se":
            return [self.anchor_x + self.width/2, self.anchor_y + self.height/2]
        elif self.anchor == "sw":
            return [self.anchor_x - self.width/2, self.anchor_y + self.height/2]
        elif self.anchor == "center":
            return [self.anchor_x, self.anchor_y]


    # 碰撞检测
    def is_collision(self,obj):
        # 四个角的坐标分别在另外一个对象的坐标区域内
        if (self.nw_pos[0] >= obj.nw_pos[0] and
                self.nw_pos[0] <= obj.se_pos[0]
                and self.nw_pos[1] >= obj.nw_pos[1]
                and self.nw_pos[1] <= obj.se_pos[1]) \
            or (self.ne_pos[0] >= obj.nw_pos[0] and
                self.ne_pos[0] <= obj.se_pos[0]
                and self.ne_pos[1] >= obj.nw_pos[1]
                and self.ne_pos[1] <= obj.se_pos[1]) \
            or (self.sw_pos[0] >= obj.nw_pos[0] and
                self.sw_pos[0] <= obj.se_pos[0]
                and self.sw_pos[1] >= obj.nw_pos[1]
                and self.sw_pos[1] <= obj.se_pos[1]) \
            or (self.se_pos[0] >= obj.nw_pos[0] and
                self.se_pos[0] <= obj.se_pos[0]
                and self.se_pos[1] >= obj.nw_pos[1]
                and self.se_pos[1] <= obj.se_pos[1]):
            return True
        else:
            return False

    '''
    爆炸效果
    把爆炸的四张图片存在列表中，
    然后边动边播放
    '''
    def explosion(self,x,y):
        self.canvas.delete(self.tag)
        # self.img_list.remove(i)
        self.img_idx += 1
        if self.img_idx < 5:
            self.exp_image = self.img_list[self.img_idx]
            self.canvas.create_image(self.center_pos[0],
                                  self.center_pos[1],
                                  anchor=tkinter.CENTER,
                                  image= self.exp_image,
                                  tags= self.tag)
            self.enemy_move(self.tag, x, y)
        else:
            self.img_list.clear()
        self.canvas.after(200, lambda :self.explosion(x,y))


    # 更新生命值
    def update_health(self):
        self.health -= 1
        if self.health <= 0:
            self.state = myconfig.status_dead
        else:
            self.state = myconfig.status_reset


    # 设置生命值
    def set_health(self,health):
        self.health = health

    # # 设置子弹移动方向
    # def set_dir(self,dir):
    #     self.blt_dir = dir




