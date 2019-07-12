'''
    界面类：
        所有的对象需要展示在画布上
'''
import tkinter
import time
import random as r
import threading
from sky import Sky
from hero import Hero
from bullet import Bullet
from bee import Bee
from bigplane import BigPlane
from smallplane import SmallPlane
from readconfig import myconfig

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


        self.window = tkinter.Tk()
        # 设置窗口尺寸
        self.window.geometry(myconfig.inter_size)
        # 设置title
        self.window.title("打飞机")
        # 不允许拖动
        self.window.resizable(0,0)

        # 添加画布
        self.cvs = tkinter.Canvas(self.window,width=myconfig.cvs_w,height=myconfig.cvs_h)
        self.cvs.pack()



        # 创建背景图片
        self.sky_1 = Sky(self.cvs,myconfig.bg_anchor_x_1,myconfig.anchor_y_1,myconfig.bg_anchor_pos_1,
                         myconfig.bg1,myconfig.bg_w,myconfig.bg_h)
        self.cvs.create_image(myconfig.bg_anchor_x_1,
                              myconfig.anchor_y_1,
                                      image=self.sky_1.bg,
                                      anchor=myconfig.bg_anchor_pos_1,
                                      tags=myconfig.bg1)
        self.sky_2 = Sky(self.cvs, self.sky_1.nw_pos[0], self.sky_1.nw_pos[1],myconfig.bg_anchor_pos_2,
                         myconfig.bg2,myconfig.bg_w,myconfig.bg_h)
        self.cvs.create_image(self.sky_1.nw_pos[0],
                                      self.sky_1.nw_pos[1],
                                      image=self.sky_2.bg,
                                      anchor=myconfig.bg_anchor_pos_2,
                                      tags=myconfig.bg2)


        # 创建英雄机
        self.hero = Hero(self.cvs,myconfig.hero_anchor_x,myconfig.hero_anchor_y,myconfig.hero_anchor,
                         myconfig.hero_tag,myconfig.hero_width,myconfig.hero_height,self.window)
        self.cvs.create_image(myconfig.hero_anchor_x,
                              myconfig.hero_anchor_y,
                               image=self.hero.img_list[0],
                               anchor=myconfig.hero_anchor,
                               tags = myconfig.hero_tag)

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
        if en.tag == myconfig.bee_tag + str(self.bee_num):
            self.score += myconfig.bee_score
        # 大飞机
        elif en.tag == myconfig.bigplane_tag + str(self.bp_num):
            self.score += myconfig.bp_score
        # 小飞机
        else:
            self.score += myconfig.sp_score
        self.cvs.itemconfigure(self.score_text,text = "分数："+str(self.score))


    # 创建大飞机
    def create_bigplane(self):
        x = r.randint(myconfig.bigplane_w,myconfig.cvs_w - myconfig.bigplane_w)
        y = -myconfig.bigplane_h/2 - 50
        self.bigplane = BigPlane(self.cvs,x, y,
                                 myconfig.anchor_bp,
                                 myconfig.bigplane_tag + str(self.bp_num),
                                 myconfig.bigplane_w,
                                 myconfig.bigplane_h)
        self.cvs.create_image(x, y,
                              anchor = myconfig.anchor_bp,
                              image = self.bigplane.img_list[0],
                              tags = myconfig.bigplane_tag + str(self.bp_num))
        self.bp_num += 1
        return self.bigplane


    # 创建小飞机
    def create_smallplane(self):
        x = r.randint(myconfig.smallplane_w, myconfig.cvs_w - myconfig.smallplane_w)
        y = -myconfig.smallplane_h / 2 - 50
        self.smallplane = SmallPlane(self.cvs, x, y,
                                     myconfig.anchor_sp,
                                     myconfig.smallplane_tag + str(self.sp_num),
                                     myconfig.smallplane_w,
                                     myconfig.smallplane_h)
        self.cvs.create_image(x, y,
                              anchor=myconfig.anchor_sp,
                              image=self.smallplane.img_list[0],
                              tags=myconfig.smallplane_tag + str(self.sp_num))
        self.sp_num += 1
        return self.smallplane


    # 创建小蜜蜂
    def create_bee(self):
        anchor_bee_x = r.randint(myconfig.bee_w/2,myconfig.cvs_w-myconfig.bee_w/2)
        bee_x_dir = r.choice([1,-1])
        self.bee = Bee(self.cvs, anchor_bee_x, -myconfig.bee_h/2 - 50,
                       myconfig.anchor_bee, myconfig.bee_tag + str(self.bee_num), myconfig.bee_w,
                       myconfig.bee_h, bee_x_dir, myconfig.cvs_w)
        self.cvs.create_image(anchor_bee_x, -myconfig.bee_h/2 - 50,
                              anchor = myconfig.anchor_bee,
                              image = self.bee.img_list[0],
                              tags = myconfig.bee_tag + str(self.bee_num))
        self.bee_num += 1
        return self.bee

    # 创建英雄机子弹
    def create_bullet(self):
        bullets = Bullet(self.cvs, self.hero.center_pos[0], self.hero.nw_pos[1] - myconfig.bullet_height / 2,
                         myconfig.bullet_anchor, myconfig.blt_tag + str(self.bullet_num),
                         myconfig.bullet_width, myconfig.bullet_height, myconfig.hero_x_dir, myconfig.hero_y_dir)
        self.cvs.create_image(self.hero.center_pos[0],
                              self.hero.nw_pos[1] - myconfig.bullet_height / 2,
                              image=bullets.bullet_img,
                              anchor=myconfig.bullet_anchor,
                              tags=myconfig.blt_tag + str(self.bullet_num))
        self.bullet_num += 1
        return bullets

    # 创建敌机子弹
    def create_en_bullet(self, en):
        en_bullets = Bullet(self.cvs, en.center_pos[0], en.sw_pos[1] - myconfig.bullet_height / 2,
                            myconfig.bullet_anchor, myconfig.blt_tag + str(self.bullet_num),
                            myconfig.bullet_width, myconfig.bullet_height, myconfig.en_x_dir, myconfig.en_y_dir)
        self.cvs.create_image(en.center_pos[0],
                              en.sw_pos[1] - myconfig.bullet_height / 2,
                              image=en_bullets.bullet_img,
                              anchor=myconfig.bullet_anchor,
                              tags=myconfig.blt_tag + str(self.bullet_num))
        self.bullet_num += 1
        return en_bullets


    # 移动背景图片
    def move_sky(self):
        # 如果背景一移动到窗口的下边沿，则把背景一移动到窗口的最上方
        if self.sky_1.nw_pos[1] >= myconfig.cvs_h:
            self.cvs.move(myconfig.bg1, 0, -(myconfig.cvs_h + myconfig.bg_h))
            self.sky_1.update_pos(0, -(myconfig.cvs_h + myconfig.bg_h))
        # 如果背景二移动到窗口的下边沿，则把背景二移动到窗口的最上方
        elif self.sky_2.nw_pos[1] >= myconfig.cvs_h:
            self.cvs.move(myconfig.bg2,0,-(myconfig.cvs_h + myconfig.bg_h))
            self.sky_2.update_pos(0, -(myconfig.cvs_h + myconfig.bg_h))
        # 否则正常移动
        else:
            self.sky_1.move()
            self.sky_2.move()


    # 移动敌机
    def move_enemy(self):
        for en in self.enemy_list:
            # 超过边界删除
            if en.nw_pos[1] > myconfig.cvs_h:
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
            if en_blt.sw_pos[1] > myconfig.cvs_h:
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
                    and en.state != myconfig.status_dead:
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
                   and en.state != myconfig.status_dead \
                   and self.hero.state == myconfig.status_alive:
                # 敌机更新生命值
                en.update_health()
                self.enemy_list.remove(en)
                self.cvs.delete(en.tag)
                # 英雄机更新生命值
                self.hero.update_health()
                # 爆炸效果
                # self.hero.explosion(0, 0)
                # 重置英雄机
                self.hero.reset_pos()
                # 更新生命值计分板
                self.cvs.itemconfigure(self.health_text,text="剩余次数："+str(self.hero.health))
                # 如果英雄机生命值耗尽则退出


        for en_blt in self.en_blt_list[:]:
             if en_blt.is_collision(self.hero)\
                 and self.hero.state != myconfig.status_dead:
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
        if self.hero.state == myconfig.status_dead:
            self.hero.play = False


    # 保存最高分
    def write_max_score(self):
        if self.score > int(myconfig.max_score):
            myconfig.update_config("game","max_score",str(self.score))
            return self.score
        else:
            return myconfig.max_score


    # 创建敌机及子弹
    def create_enemy(self):
        # 每1帧创建一颗英雄机子弹
        if self.count % myconfig.blt_fre == 0:
            bullets = self.create_bullet()
            self.blt_list.append(bullets)

        # 每50帧创建一颗敌机子弹
        if self.count % myconfig.en_blt_fre == 0:
            for en in self.enemy_list:
                if en.tag != myconfig.bee_tag + str(self.bee_num):
                    en_bullets = self.create_en_bullet(en)
                    self.en_blt_list.append(en_bullets)

        # 每35帧创建一个小蜜蜂
        if self.count % myconfig.bee_fre == 0:
            bees = self.create_bee()
            self.enemy_list.append(bees)

        # 每100帧创建一个大飞机
        if self.count % myconfig.bp_fre == 0:
            bps = self.create_bigplane()
            self.enemy_list.append(bps)

        # 每20帧创建一个小飞机
        if self.count % myconfig.sp_fre == 0:
            sps = self.create_smallplane()
            self.enemy_list.append(sps)


    # 结束游戏,打印分数
    def end_game(self):
        self.cvs.create_text(200, 350, fill="green",
                             text="游戏结束！\r\n当前成绩：{0}\r\n最高成绩：{1}".format(self.score, self.write_max_score()),
                             font=["宋体", 20])


    # 退出游戏
    def quit_game(self):
        self.cvs.quit()

    # 接收键盘事件
    def recv_event(self, e):
        if e.keysym == "Return":  # 按回车键开始游戏
            self.start_game()
        elif e.keysym == "Escape":  # Esc退出游戏
            self.quit_game()


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

            # 创建敌机及子弹
            self.create_enemy()

            self.count += 1

        # 如果生命值耗尽则打印成绩
        else:
            self.end_game()

        self.cvs.after(50, self.start_game)


if __name__ == '__main__':
    inter = Interface()
    inter.window.mainloop()


