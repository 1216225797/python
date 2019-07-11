'''
    界面类：
        所有的对象需要展示在画布上
'''
import tkinter
from configparser import ConfigParser
import time
import random as r
import threading
from sky import Sky
from hero import Hero
from bullet import Bullet
from bee import Bee
from bigplane import BigPlane
from smallplane import SmallPlane

class Interface():
    def __init__(self):
        # 记录屏幕上各个部件移动的次数，
        # 控制各个部件移动的频率
        self.count = 0
        # 存放英雄机子弹对象
        self.blt_list = []
        # 存放敌机子弹对象
        self.en_blt_list = []
        # 记录子弹的数量
        self.bullet_num = 0
        # 记录小蜜蜂数量
        self.bee_num = 0
        # 记录大飞机数量
        self.bp_num = 0
        # 记录小飞机数量
        self.sp_num = 0
        # 存放敌方对象
        self.enemy_list = []
        # 击落敌军数量
        self.enemy_down_num = 0
        # 分数
        self.score = 0



        # 初始化类
        self.conf = ConfigParser()
        self.conf.read("config.ini",encoding="UTF-8")
        # 窗口尺寸
        inter_size = self.conf.get("interface","inter_size")
        # 画布宽高
        self.cvs_w = self.conf.getint("interface","canvas_width")
        self.cvs_h = self.conf.getint("interface", "canvas_height")

        # 背景的移动速度
        speed = (self.conf.get("background", "x_step"), self.conf.get("background", "y_step"))
        # 背景一图片锚点位置
        self.bg_anchor_pos_1 = self.conf.get("background", "anchor_1")
        # 背景一图片锚点坐标
        self.bg_anchor_x_1 = self.conf.getint("background", "anchor_x_1")
        self.anchor_y_1 = self.conf.getint("background", "anchor_y_1")
        # 背景二
        self.bg_anchor_pos_2 = self.conf.get("background", "anchor_2")
        # self.bg_anchor_x_2 = self.conf.getint("background", "anchor_x_2")
        # self.bg_anchor_y_2 = self.conf.getint("background", "anchor_y_2")

        # 背景宽高
        self.bg_w = self.conf.getint("background", "w")
        self.bg_h = self.conf.getint("background", "h")
        # tag
        self.bg1 = self.conf.get("background", "tag_1")
        self.bg2 = self.conf.get("background", "tag_2")

        # 英雄机
        self.hero_anchor = self.conf.get("hero","anchor")
        self.hero_anchor_x = self.conf.getint("hero","anchor_x")
        self.hero_anchor_y = self.conf.getint("hero","anchor_y")
        self.hero_tag = self.conf.get("hero", "tag")
        self.hero_width = self.conf.getint("hero", "width")
        self.hero_height = self.conf.getint("hero", "height")

        # 子弹
        self.bullet_anchor = self.conf.get("bullet", "anchor")
        self.blt_tag = self.conf.get("bullet","tag")
        self.bullet_width = self.conf.getint("bullet","width")
        self.bullet_height = self.conf.getint("bullet", "height")
        self.blt_fre = self.conf.getint("bullet","fre")
        self.en_blt_fre = self.conf.getint("bullet","en_fre")
        self.hero_x_dir = self.conf.getint("bullet","hero_x_dir")
        self.hero_y_dir = self.conf.getint("bullet", "hero_y_dir")
        self.en_x_dir = self.conf.getint("bullet", "en_x_dir")
        self.en_y_dir = self.conf.getint("bullet", "en_y_dir")

        # 小蜜蜂
        self.bee_w = self.conf.getint("bee","width")
        self.bee_h = self.conf.getint("bee","height")
        self.anchor_bee = self.conf.get("bee","anchor")
        self.bee_tag = self.conf.get("bee","tag")
        # 小蜜蜂创建频率
        self.bee_fre = self.conf.getint("bee", "fre")


        # 大飞机
        self.bigplane_tag = self.conf.get("bigplane","tag")
        self.bigplane_w = self.conf.getint("bigplane", "width")
        self.bigplane_h = self.conf.getint("bigplane","height")
        self.anchor_bp = self.conf.get("bigplane","anchor")
        # 创建大飞机频率
        self.bp_fre = self.conf.getint("bigplane", "fre")

        # 小飞机
        self.smallplane_tag = self.conf.get("smallplane", "tag")
        self.smallplane_w = self.conf.getint("smallplane", "width")
        self.smallplane_h = self.conf.getint("smallplane", "height")
        self.anchor_sp = self.conf.get("smallplane", "anchor")
        # 创建大飞机频率
        self.sp_fre = self.conf.getint("smallplane", "fre")

        # 分数
        self.bee_score = self.conf.getint("game","bee_score")
        self.bp_score = self.conf.getint("game", "bp_score")
        self.sp_score = self.conf.getint("game", "sp_score")
        self.max_score = self.conf.get("game","max_score")


        self.window = tkinter.Tk()
        # 设置窗口尺寸
        self.window.geometry(inter_size)
        # 设置title
        self.window.title("打飞机")
        # 不允许拖动
        self.window.resizable(0,0)

        # 添加画布
        self.cvs = tkinter.Canvas(self.window,width=self.cvs_w,height=self.cvs_h)
        self.cvs.pack()



        # 创建背景图片
        self.sky_1 = Sky(self.cvs,self.bg_anchor_x_1,self.anchor_y_1,self.bg_anchor_pos_1,
                         self.bg1,self.bg_w,self.bg_h)
        self.cvs.create_image(self.bg_anchor_x_1,
                                      self.anchor_y_1,
                                      image=self.sky_1.bg,
                                      anchor=self.bg_anchor_pos_1,
                                      tags=self.bg1)
        self.sky_2 = Sky(self.cvs, self.sky_1.nw_pos[0], self.sky_1.nw_pos[1],self.bg_anchor_pos_2,
                         self.bg2,self.bg_w,self.bg_h)
        self.cvs.create_image(self.sky_1.nw_pos[0],
                                      self.sky_1.nw_pos[1],
                                      image=self.sky_2.bg,
                                      anchor=self.bg_anchor_pos_2,
                                      tags=self.bg2)


        # 创建英雄机
        self.hero = Hero(self.cvs,self.hero_anchor_x,self.hero_anchor_y,self.hero_anchor,
                         self.hero_tag,self.hero_width,self.hero_height,self.window)
        self.cvs.create_image(self.hero_anchor_x,
                              self.hero_anchor_y,
                               image=self.hero.img_list[0],
                               anchor=self.hero_anchor,
                               tags = self.hero.tag)

        # 创建分数框
        self.score_text = self.cvs.create_text(15, 10,
                             text="分数：0",
                             fill="red",
                             font=("宋体", 15),
                             anchor=tkinter.NW)
        # 生命值
        self.health_text = self.cvs.create_text(385, 10,
                                                text="剩余次数："+str(self.hero.health),
                                                fill="blue",
                                                font=("宋体", 15),
                                                anchor=tkinter.NE)

        # 绑定事件
        self.window.bind("<Return>", lambda e: self.recv_event(e))
        self.window.bind("<KeyPress-Escape>", lambda e: self.recv_event(e))
        # self.window.bind("<KeyPress-space>", lambda e: self.recv_event(e))


    # 计分并更新计分板
    def count_score(self,en):
        # 小蜜蜂
        if en.tag == self.bee_tag + str(self.bee_num):
            self.score += self.bee_score
        # 大飞机
        elif en.tag == self.bigplane_tag + str(self.bp_num):
            self.score += self.bp_score
        # 小飞机
        else:
            self.score += self.sp_score
        self.cvs.itemconfigure(self.score_text,text = "分数："+str(self.score))



    # 创建大飞机
    def create_bigplane(self):
        x = r.randint(self.bigplane_w,self.cvs_w - self.bigplane_w)
        y = -self.bigplane_h/2 - 50
        self.bigplane = BigPlane(self.cvs,x, y,
                                 self.anchor_bp,
                                 self.bigplane_tag + str(self.bp_num),
                                 self.bigplane_w,
                                 self.bigplane_h)
        self.cvs.create_image(x, y,
                              anchor = self.anchor_bp,
                              image = self.bigplane.img_list[0],
                              tags = self.bigplane_tag + str(self.bp_num))
        self.bp_num += 1
        return self.bigplane


    # 创建小飞机
    def create_smallplane(self):
        x = r.randint(self.smallplane_w, self.cvs_w - self.smallplane_w)
        y = -self.smallplane_h / 2 - 50
        self.smallplane = SmallPlane(self.cvs, x, y,
                                 self.anchor_sp,
                                 self.smallplane_tag + str(self.sp_num),
                                 self.smallplane_w,
                                 self.smallplane_h)
        self.cvs.create_image(x, y,
                              anchor=self.anchor_sp,
                              image=self.smallplane.img_list[0],
                              tags=self.smallplane_tag + str(self.sp_num))
        self.sp_num += 1
        return self.smallplane


    # 创建小蜜蜂
    def create_bee(self):
        anchor_bee_x = r.randint(self.bee_w/2,self.cvs_w-self.bee_w/2)
        bee_x_dir = r.choice([1,-1])
        self.bee = Bee(self.cvs, anchor_bee_x, -self.bee_h/2 - 50,
                  self.anchor_bee, self.bee_tag + str(self.bee_num), self.bee_w,
                  self.bee_h, bee_x_dir, self.cvs_w)
        self.cvs.create_image(anchor_bee_x, -self.bee_h/2 - 50,
                              anchor = self.anchor_bee,
                              image = self.bee.img_list[0],
                              tags = self.bee_tag + str(self.bee_num))
        self.bee_num += 1
        return self.bee

    # 创建英雄机子弹
    def create_bullet(self):
        bullets = Bullet(self.cvs, self.hero.center_pos[0], self.hero.nw_pos[1] - self.bullet_height / 2,
                         self.bullet_anchor, self.blt_tag + str(self.bullet_num),
                         self.bullet_width, self.bullet_height, self.hero_x_dir, self.hero_y_dir)
        self.cvs.create_image(self.hero.center_pos[0],
                              self.hero.nw_pos[1] - self.bullet_height / 2,
                              image=bullets.bullet_img,
                              anchor=self.bullet_anchor,
                              tags=self.blt_tag + str(self.bullet_num))
        self.bullet_num += 1
        return bullets

    # 创建敌机子弹
    def create_en_bullet(self, en):
        en_bullets = Bullet(self.cvs, en.center_pos[0], en.sw_pos[1] - self.bullet_height / 2,
                            self.bullet_anchor, self.blt_tag + str(self.bullet_num),
                            self.bullet_width, self.bullet_height, self.en_x_dir, self.en_y_dir)
        self.cvs.create_image(en.center_pos[0],
                              en.sw_pos[1] - self.bullet_height / 2,
                              image=en_bullets.bullet_img,
                              anchor=self.bullet_anchor,
                              tags=self.blt_tag + str(self.bullet_num))
        self.bullet_num += 1
        return en_bullets


    def move_sky(self):
        # 如果背景一移动到窗口的下边沿，则把背景一移动到窗口的最上方
        if self.sky_1.nw_pos[1] >= self.cvs_h:
            self.cvs.move(self.bg1, 0, -(self.cvs_h + self.bg_h))
            self.sky_1.update_pos(0, -(self.cvs_h + self.bg_h))
        # 如果背景二移动到窗口的下边沿，则把背景二移动到窗口的最上方
        elif self.sky_2.nw_pos[1] >= self.cvs_h:
            self.cvs.move(self.bg2,0,-(self.cvs_h + self.bg_h))
            self.sky_2.update_pos(0, -(self.cvs_h + self.bg_h))
        # 否则正常移动
        else:
            self.sky_1.move()
            self.sky_2.move()


    # 移动敌机
    def move_enemy(self):
        for en in self.enemy_list:
            # 超过边界删除
            if en.nw_pos[1] > self.cvs_h:
                self.enemy_list.remove(en)
                self.cvs.delete(en.tag)
            else:
                en.move()

    # 移动子弹
    def move_blt(self):
        for blt in self.blt_list:
            # 超过边界删除
            if blt.nw_pos[1] < 0:
                self.blt_list.remove(blt)
                self.cvs.delete(blt.tag)
            else:
                blt.move()
        for en_blt in self.en_blt_list[:]:
            # 超过边界删除
            if en_blt.sw_pos[1] > self.cvs_h:
                self.en_blt_list.remove(en_blt)
                self.cvs.delete(en_blt.tag)
            else:
                en_blt.move()
    # 碰撞
    def check_collision(self):
        # 子弹和敌机相撞
        '''
        这里需要注意：在迭代器中直接删除列表元素很危险，
        因为迭代器是直接引用列表元素数据做操作(传址)
        所以把列表拷贝一份传给迭代器，再对原列表进行操作
        '''
        for en in self.enemy_list[:]:
            # 如果英雄机子弹和敌机相撞则删除敌机对象和图片
            for each_blt in self.blt_list[:]:
                if each_blt.is_collision(en) \
                    and en.state != en.conf.getint("game","status_dead"):
                    # 更新分数计分板
                    self.count_score(en)
                    # 更新生命值
                    en.update_health()
                    # 爆炸效果
                    en.explosion(en.speed[0], en.speed[1])
                    self.enemy_list.remove(en)
                    self.cvs.delete(en.tag)
                    self.blt_list.remove(each_blt)
                    self.cvs.delete(each_blt.tag)

            # 如果英雄机和敌机相撞
            if en.is_collision(self.hero) \
                   and en.state != en.conf.getint("game", "status_dead") \
                   and self.hero.state != self.conf.getint("game","status_dead"):
                # 敌机更新生命值
                en.update_health()
                self.enemy_list.remove(en)
                self.cvs.delete(en.tag)
                # 英雄机更新生命值
                self.hero.update_health()
                # if self.hero.state == self.conf.getint("game","status_alive"):
                # 爆炸效果
                # self.hero.explosion(0, 0)
                # 重置英雄机
                self.hero.reset_pos()
                # 更新生命值计分板
                self.cvs.itemconfigure(self.health_text,text="剩余次数："+str(self.hero.health))
                # 如果英雄机生命值耗尽则退出


        for en_blt in self.en_blt_list[:]:
             if en_blt.is_collision(self.hero)\
                 and self.hero.state != self.conf.getint("game","status_dead"):
                 self.en_blt_list.remove(en_blt)
                 self.cvs.delete(en_blt.tag)
                 # 英雄机更新生命值
                 self.hero.update_health()
                 # 爆炸效果
                 # self.hero.explosion(0, 0)
                 # 重置英雄机
                 self.hero.reset_pos()
                 # 更新生命值计分板
                 self.cvs.itemconfigure(self.health_text, text="剩余次数：" + str(self.hero.health))
        # 如果英雄机生命值耗尽则退出
        if self.hero.state == self.conf.getint("game", "status_dead"):
            self.hero.play = False


    # 保存最高分
    def write_max_score(self):
        if self.score > int(self.max_score):
            self.conf.set("game", "max_score", str(self.score))
            # 保存config
            self.conf.write(open("config.ini","w"))
            return self.score
        else:
            return self.max_score



    # 开始游戏
    def start_game(self):
        if self.hero.play:
            # 移动天空
            self.move_sky()
            # 移动敌机
            self.move_enemy()
            # 移动子弹
            self.move_blt()

            # 碰撞检测
            self.check_collision()

            self.window.update()

            # 每1帧创建一颗英雄机子弹
            if self.count % self.blt_fre == 0:
                bullets = self.create_bullet()
                self.blt_list.append(bullets)

            # 每4帧创建一颗敌机子弹
            if self.count % self.en_blt_fre == 0:
                for en in self.enemy_list:
                    if en.tag != self.bee_tag + str(self.bee_num):
                        en_bullets = self.create_en_bullet(en)
                        self.en_blt_list.append(en_bullets)

            # 每30帧创建一个小蜜蜂
            if self.count % self.bee_fre == 0:
                bees = self.create_bee()
                self.enemy_list.append(bees)

            # 每70帧创建一个大飞机
            if self.count % self.bp_fre == 0:
                bps = self.create_bigplane()
                self.enemy_list.append(bps)

            # 每10帧创建一个小飞机
            if self.count % self.sp_fre == 0:
                sps = self.create_smallplane()
                self.enemy_list.append(sps)

            self.count += 1

        # 如果生命值耗尽则打印成绩
        else:
            self.end_game()

        self.cvs.after(50, self.start_game)

    # 结束游戏,打印分数
    def end_game(self):
        self.cvs.create_text(200, 350, fill="green",
                             text="游戏结束！\r\n当前成绩：{0}\r\n最高成绩：{1}".format(self.score,self.write_max_score()),
                             font = ["宋体",20])

    # def restart_game(self):
    #     # self.hero.play = True
    #     self.__init__()

    # 退出游戏
    def quit_game(self):
        self.cvs.quit()

    # 接收事件
    def recv_event(self,e):
        if e.keysym == "Return": # 按回车键开始游戏
            self.start_game()
        elif e.keysym == "Escape": # Esc退出游戏
            self.quit_game()
        # elif e.keysym == "space": # 空格重新开始
        #     self.restart_game()



if __name__ == '__main__':
    inter = Interface()
    inter.window.mainloop()


