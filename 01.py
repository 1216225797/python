'''
定义一个学生类，用来描述学生
'''


class Student():
    # 可以用None给不确定的值赋值
    name = None
    age = 18
    sex =  'girl'

    def run(self):
        # 需要注意：
        # 1.def run()的缩进层级
        # 2.系统默认出一个self参数
        print("我要好好锻炼身体")
        # 推荐在函数末尾使用return语句
        return None


# 实例化一个叫xiaoguo的具体的人
xiaoguo = Student()

print(xiaoguo.name)
print(xiaoguo.age)
print(xiaoguo.sex)

# 注意成员函数的调用没有传递参数
xiaoguo.run()

print(xiaoguo.__dict__)
print(Student.__dict__)