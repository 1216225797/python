'''
飞机大战验证v02:
    让背景图和小蜜蜂动起来
    小飞机和大飞机只垂直向下移动
    小蜜蜂是横向和纵向同时移动，并且碰到墙壁时，弹回(即y轴不变,x轴相反)
    小飞机和小蜜蜂的x轴出现位置随机
    天空背景移动算法：
        1.创建两张天空图片的实例
        2.第二张图片放在第一张图片的上方，当第一张开始移动时，第二张跟着一起移动
        3.等到第一张移动到窗口最下方，立即切换到第二张的上方，如此循环即可做到无缝衔接
'''
import tkinter
import random

# 画布的宽和高
w = 450
h = 700
# 天空背景的宽高
image_sky_width = 480
image_sky_height = 852

# 小蜜蜂随机出现的横坐标
bee_x = random.randrange(40,w-40)
bee_y = 60
# 天空_1背景的左上角y坐标
sky_1_nw_y = 0
# 天空_2背景的左上角y坐标
sky_2_sw_y = -852
# 小飞机随机出现的横坐标
small_aircraft_x = random.randrange(30,w-30)
small_aircraft_y = -30
# 飞机移动速度
x_step = 5
y_step = 5

def small_aircraft_move():
    # 小飞机一直往下移动，所以x轴不变，y轴增加
    '''
     coords()方法和move()方法的区别:
     1.coords()可以改变图形的大小,后者不可以
     2.coords()中传入的参数表示更新后的坐标；move()中的参数表示坐标需要移动的距离
    '''
    # 移动速度

    global small_aircraft_y,small_aircraft_x
    global x_step,y_step

    small_aircraft_x += x_step
    small_aircraft_y += y_step


    if small_aircraft_x >= w-30 or small_aircraft_x <= 30:
        x_step = -x_step
        # print(small_aircraft_x)

    cvs.move("small_aircraft",x_step,y_step)
    cvs.after(100,small_aircraft_move)
    # print(small_aircraft_x, small_aircraft_y)
# def bee_move():
#     cvs.move("bee",bee_x,bee_y)
#     print(bee_x,bee_y)
#     cvs.after(200,bee_move)


def move_sky():
    global sky_step
    global sky_1_nw_y
    global sky_2_sw_y
    if sky_1_nw_y >= h:
        cvs.move("bg1",0,-(h+image_sky_height))
        sky_1_nw_y = -image_sky_height
        print(sky_1_nw_y)
    elif sky_2_sw_y >= h:
        cvs.move("bg2", 0, -(h + image_sky_height))
        sky_2_sw_y = -image_sky_height
    else:
        cvs.move("bg1", 0, 10)
        cvs.move("bg2", 0, 10)
    sky_1_nw_y += 10
    sky_2_sw_y += 10
    print(sky_1_nw_y)
    cvs.after(200, move_sky)


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
# 创建天空背景实例
bgimg_1 = tkinter.PhotoImage(file=bgpath)
bgimg_2 = tkinter.PhotoImage(file=bgpath)

small_aircraft_img = tkinter.PhotoImage(file=small_aircraft_path)
bee_image = tkinter.PhotoImage(file=bee_path)
# print(small_aircraft_img)



cvs = tkinter.Canvas(root,width=w,height=h)
# 背景图片的坐标,锚点默认为center
sky1=cvs.create_image(0,0,image=bgimg_1,anchor=tkinter.NW,tags="bg1")
sky2=cvs.create_image(0,0,image=bgimg_2,anchor=tkinter.SW,tags="bg2")
move_sky()

cvs.create_image(small_aircraft_x,small_aircraft_y,image=small_aircraft_img,tags="small_aircraft")
cvs.create_image(bee_x,bee_y,image=bee_image)
small_aircraft_move()
# bee_move()
# print(small_aircraft_x,small_aircraft_y)
cvs.pack()

root.mainloop()
