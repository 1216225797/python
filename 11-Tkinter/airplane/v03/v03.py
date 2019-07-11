'''
    飞机大战验证v03：
        生成英雄级并发射子弹
        打掉敌机消失，并加分

    anchor(锚点)的作用：
        生成图片的坐标点作用于定义的锚点上(即相对于图片的点)
        默认CENTER
'''
import tkinter
import random
import time

# 画布的宽和高
w = 450
h = 700

# 天空背景的宽高
image_sky_width = 480
image_sky_height = 852

# 小蜜蜂随机出现的横坐标
bee_x = random.randrange(40,w-40)
bee_y = -30

# 天空_1背景的左上角y坐标
sky_1_nw_y = 0
# 天空_2背景的左上角y坐标
sky_2_sw_y = -852

# 小飞机随机出现的横坐标
small_aircraft_x = random.randrange(30,w-30)
small_aircraft_y = -30
# 小飞机的宽和高
small_aircraft_width = 49
small_aircraft_height = 36

# 飞机移动速度
x_step = 5
y_step = 5
# 英雄机初始坐标
hero_x_pos = 225
hero_y_pos = 650

# 英雄机的宽高
hero_width=97
hero_height=124

# 子弹的初始坐标
bullet_x = hero_x_pos
bullet_y = hero_y_pos - hero_height / 2

# 子弹数量
bullet_num = 1

# 存放子弹
bullet_list = list()

def bee_move():
    # 小飞机一直往下移动，所以x轴不变，y轴增加
    '''
     coords()方法和move()方法的区别:
     1.coords()可以改变图形的大小,后者不可以
     2.coords()中传入的参数表示更新后的坐标；move()中的参数表示坐标需要移动的距离
    '''
    # 移动速度

    global bee_x,bee_y
    global x_step,y_step

    bee_x += x_step
    bee_y += y_step


    if bee_x >= w-30 or bee_x <= 30:
        x_step = -x_step
        # print(small_aircraft_x)

    cvs.move("bee",x_step,y_step)
    cvs.after(100,bee_move)

def small_airplane_move():
    cvs.move("small_aircraft",0,5)
    cvs.after(100,small_airplane_move)

def hero_move(e):
    global hero_x_pos
    global hero_y_pos
    if e.keysym == "Up":
        cvs.move("hero",0,-10)
        hero_y_pos -= 10
    if e.keysym == "Down":
        cvs.move("hero", 0, 10)
        hero_y_pos += 10
    if e.keysym == "Left":
        cvs.move("hero", -10, 0)
        hero_x_pos -= 10
    if e.keysym == "Right":
        cvs.move("hero", 10, 0)
        hero_x_pos += 10
    # print(e.keysym)
    # print(hero_x_pos,hero_y_pos)



def move_sky():
    global sky_step
    global sky_1_nw_y
    global sky_2_sw_y
    if sky_1_nw_y >= h:
        cvs.move("bg1",0,-(h+image_sky_height))
        sky_1_nw_y = -image_sky_height
    elif sky_2_sw_y >= h:
        cvs.move("bg2", 0, -(h + image_sky_height))
        sky_2_sw_y = -image_sky_height
    else:
        cvs.move("bg1", 0, 10)
        cvs.move("bg2", 0, 10)
    sky_1_nw_y += 10
    sky_2_sw_y += 10
    # print(sky_1_nw_y)
    cvs.after(200, move_sky)

def bullet_move():
    global bullet_num
    global bullet_x
    global bullet_y
    global hero_x_pos,hero_y_pos
    # tag = "bullet" + str(bullet_num)
    bullet_img = cvs.create_image(hero_x_pos, hero_y_pos - hero_height / 2, image=bullet_image, tags="bullet"+str(bullet_num))
    bullet_list.append(bullet_img)
    for i in bullet_list:
        cvs.move(i,0,-20)
        bullet_y -= 20
        print(bullet_x,bullet_y)
        # print("bullet"+str(i)+"的坐标是：{0}".format(bullet_pos))
    bullet_num += 1
    # bullet_y -= 10
    cvs.after(100,bullet_move)

# 获取小飞机机每个点的坐标
def get_small_airplane_pos():
    # 默认锚点为center
    # 左上角
    small_airplane_nw_pos = small_aircraft_x - small_aircraft_width/2,small_aircraft_y - small_aircraft_height/2
    # 右上角
    small_airplane_ne_pos = small_aircraft_x + small_aircraft_width/2,small_aircraft_y - small_aircraft_height/2
    # 右下角
    small_airplane_se_pos = small_aircraft_x + small_aircraft_width/2,small_aircraft_y + small_aircraft_height/2
    # 左下角
    small_airplane_sw_pos = small_aircraft_x - small_aircraft_width/2,small_aircraft_y + small_aircraft_height/2
    # 中心点
    small_airplane_center_pos = small_aircraft_x,small_aircraft_x

    return small_airplane_nw_pos,small_airplane_ne_pos,small_airplane_se_pos,small_airplane_sw_pos



root = tkinter.Tk()
# 设置边框的大小
root.geometry("450x700")
# 不允许拖动边框大小
root.resizable(0,0)

'''
创建图片三步骤:
    1.定义图片位置
    2.实例化PhotoImage对象
    3.create_image创建图片
'''
bgpath = r"D:\PycharmProjects\study\11-Tkinter\airplane\images\background.gif"
small_aircraft_path = r"D:\PycharmProjects\study\11-Tkinter\airplane\images\smallplane.gif"
bee_path = r"..\images\bee.gif"
hero_path = r"..\images\hero.gif"
bullet_path = r"..\images\bullet.gif"
# 创建天空背景实例
bgimg_1 = tkinter.PhotoImage(file=bgpath)
bgimg_2 = tkinter.PhotoImage(file=bgpath)

# 创建小飞机实例
small_aircraft_img = tkinter.PhotoImage(file=small_aircraft_path)

# 创建小蜜蜂实例
bee_image = tkinter.PhotoImage(file=bee_path)

# 创建英雄机实例
hero_image = tkinter.PhotoImage(file=hero_path)

# 创建子弹实例
bullet_image = tkinter.PhotoImage(file=bullet_path)

cvs = tkinter.Canvas(root,width=w,height=h)
# 背景图片的坐标,锚点默认为center
sky1=cvs.create_image(0,0,image=bgimg_1,anchor=tkinter.NW,tags="bg1")
sky2=cvs.create_image(0,0,image=bgimg_2,anchor=tkinter.SW,tags="bg2")
move_sky()

cvs.create_image(small_aircraft_x,small_aircraft_y,image=small_aircraft_img,tags="small_aircraft")
cvs.create_image(bee_x,bee_y,image=bee_image,tags="bee")
cvs.create_image(hero_x_pos,hero_y_pos,image=hero_image,tags="hero",anchor=tkinter.CENTER)
# print(hero_x_pos,hero_y_pos)
# 绑定事件
root.bind("<Key-Up>",hero_move)
root.bind("<Key-Down>",hero_move)
root.bind("<Key-Left>",hero_move)
root.bind("<Key-Right>",hero_move)

bee_move()
small_airplane_move()
bullet_move()
# bee_move()
# print(small_aircraft_x,small_aircraft_y)
cvs.pack()

root.mainloop()
