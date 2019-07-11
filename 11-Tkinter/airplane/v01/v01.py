'''
飞机大战验证v01:
    显示背景和小飞机
'''

import tkinter

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
bgpath1 = r"D:\PycharmProjects\study\11-Tkinter\airplane\images\background.gif"
bgpath2 = r"D:\PycharmProjects\study\11-Tkinter\airplane\images\bee.gif"
bgimg1 = tkinter.PhotoImage(file=bgpath1)
bgimg2 = tkinter.PhotoImage(file=bgpath2)
cvs = tkinter.Canvas(root,width=450,height=700)
cvs.create_image(220,270,image=bgimg1)
cvs.create_image(50,50,image=bgimg2)
cvs.pack()

root.mainloop()