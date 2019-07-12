'''
    实例化配置文件
'''

from configparser import ConfigParser

class MyConfig():
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read("config.ini",encoding="utf-8")

        # 窗口尺寸
        self.inter_size = self.conf.get("interface", "inter_size")
        # 画布宽高
        self.cvs_w = self.conf.getint("interface", "canvas_width")
        self.cvs_h = self.conf.getint("interface", "canvas_height")

        # 背景的移动速度
        self.bg_x_step = self.conf.getint("background", "x_step")
        self.bg_y_step = self.conf.getint("background", "y_step")
        # 背景一图片锚点位置
        self.bg_anchor_pos_1 = self.conf.get("background", "anchor_1")
        # 背景一图片锚点坐标
        self.bg_anchor_x_1 = self.conf.getint("background", "anchor_x_1")
        self.anchor_y_1 = self.conf.getint("background", "anchor_y_1")
        # 背景二
        self.bg_anchor_pos_2 = self.conf.get("background", "anchor_2")

        # 背景宽高
        self.bg_w = self.conf.getint("background", "w")
        self.bg_h = self.conf.getint("background", "h")
        # tag
        self.bg1 = self.conf.get("background", "tag_1")
        self.bg2 = self.conf.get("background", "tag_2")
        self.bg_img_path = self.conf.get("background","path")
        self.bg_x_dir = self.conf.getint("background","x_dir")
        self.bg_y_dir = self.conf.getint("background", "y_dir")


        # 英雄机
        self.hero_anchor = self.conf.get("hero", "anchor")
        self.hero_anchor_x = self.conf.getint("hero", "anchor_x")
        self.hero_anchor_y = self.conf.getint("hero", "anchor_y")
        self.hero_tag = self.conf.get("hero", "tag")
        self.hero_width = self.conf.getint("hero", "width")
        self.hero_height = self.conf.getint("hero", "height")
        self.hero_x_step = self.conf.getint("hero","x_step")
        self.hero_y_step = self.conf.getint("hero", "y_step")
        self.hero_img_path = self.conf.get("hero", "img_path")
        self.hero_img_suffix = self.conf.get("hero", "suffix")

        # 子弹
        self.bullet_anchor = self.conf.get("bullet", "anchor")
        self.blt_tag = self.conf.get("bullet", "tag")
        self.bullet_width = self.conf.getint("bullet", "width")
        self.bullet_height = self.conf.getint("bullet", "height")
        self.blt_fre = self.conf.getint("bullet", "fre")
        self.en_blt_fre = self.conf.getint("bullet", "en_fre")
        self.hero_x_dir = self.conf.getint("bullet", "hero_x_dir")
        self.hero_y_dir = self.conf.getint("bullet", "hero_y_dir")
        self.en_x_dir = self.conf.getint("bullet", "en_x_dir")
        self.en_y_dir = self.conf.getint("bullet", "en_y_dir")
        self.bullet_x_step = self.conf.getint("bullet", "x_step")
        self.bullet_y_step = self.conf.getint("bullet", "y_step")
        self.bullet_img_path = self.conf.get("bullet","bullet_img_path")

        # 小蜜蜂
        self.bee_w = self.conf.getint("bee", "width")
        self.bee_h = self.conf.getint("bee", "height")
        self.anchor_bee = self.conf.get("bee", "anchor")
        self.bee_tag = self.conf.get("bee", "tag")
        # 小蜜蜂创建频率
        self.bee_fre = self.conf.getint("bee", "fre")
        self.bee_x_step = self.conf.getint("bee","x_step")
        self.bee_y_step = self.conf.getint("bee", "y_step")
        self.bee_img_path = self.conf.get("bee","img_path")
        self.bee_img_suffix = self.conf.get("bee","suffix")

        # 大飞机
        self.bigplane_tag = self.conf.get("bigplane", "tag")
        self.bigplane_w = self.conf.getint("bigplane", "width")
        self.bigplane_h = self.conf.getint("bigplane", "height")
        self.anchor_bp = self.conf.get("bigplane", "anchor")
        # 创建大飞机频率
        self.bp_fre = self.conf.getint("bigplane", "fre")
        self.bp_x_step = self.conf.getint("bigplane", "x_step")
        self.bp_y_step = self.conf.getint("bigplane", "y_step")
        self.bp_x_dir = self.conf.getint("bigplane", "x_dir")
        self.bp_y_dir = self.conf.getint("bigplane", "y_dir")
        self.bp_img_path = self.conf.get("bigplane", "img_path")
        self.bp_img_suffix = self.conf.get("bigplane", "suffix")

        # 小飞机
        self.smallplane_tag = self.conf.get("smallplane", "tag")
        self.smallplane_w = self.conf.getint("smallplane", "width")
        self.smallplane_h = self.conf.getint("smallplane", "height")
        self.anchor_sp = self.conf.get("smallplane", "anchor")
        # 创建小飞机频率
        self.sp_fre = self.conf.getint("smallplane", "fre")
        self.sp_x_step = self.conf.getint("smallplane", "x_step")
        self.sp_y_step = self.conf.getint("smallplane", "y_step")
        self.sp_x_dir = self.conf.getint("smallplane", "x_dir")
        self.sp_y_dir = self.conf.getint("smallplane", "y_dir")
        self.sp_img_path = self.conf.get("smallplane", "img_path")
        self.sp_img_suffix = self.conf.get("smallplane", "suffix")


        # 分数
        self.bee_score = self.conf.getint("game", "bee_score")
        self.bp_score = self.conf.getint("game", "bp_score")
        self.sp_score = self.conf.getint("game", "sp_score")
        self.max_score = self.conf.get("game", "max_score")


        # 游戏参数
        self.status_alive = self.conf.getint("game","status_alive")
        self.status_dead = self.conf.getint("game","status_dead")
        self.status_reset = self.conf.getint("game","status_reset")
        self.enemy_health = self.conf.getint("game","enemy_health")
        self.hero_health = self.conf.getint("game","hero_health")

    # 修改配置文件
    def update_config(self,opt,name,value):
        self.conf.set(opt,name,value)
        # 写法一：
        self.conf.write(open("config.ini", "w"))
        # 写法二：
        # with open("config.ini","w",encoding="utf-8") as f:
        #     self.conf.write(f)
myconfig = MyConfig()
