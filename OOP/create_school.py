# 创建北京和成都两个校区
# 创建Linux/Python两个课程
# 创建北京校区的Python3期课程和成都校区的Linux一期课程
# 管理员创建了北京校区的学员小张，并将其分配在了python3期课程
# 管理员创建了讲师小周，并将其分配在了Python3期
# 讲师小周为Day02这节课所有的学员批改了作业，小张得了A，小王得了B
# 学员小张查看了自己所报的课程
# 学员小张在查看了自己在Python3的成绩列表然后退出了
# 学员小张给了讲师小周好评

'''
class School():
    def __init__(self,school_name):
        self.school_name = school_name


    def create_teacher(self,tea_name):
        self.teacher = tea_name
        print("欢迎{0}老师的加入！".format(self.teacher))

    def create_student(self,stu_name):
        self.student = stu_name
        print("欢迎{0}同学的加入！".format(self.stuent))

'''


class Campus():
    def __init__(self, school_name, course, code):
        # get_teacher = self.teacher.append(teacher)
        # get_student = self.student.append(studnet)
        self.school_name = school_name
        self.course = course
        self.code = code

        print("已成功创建{0}校区{1}{2}课程".format(self.school_name, self.course, self.code))

    def course_info(self):
        print("{}的课程大纲是：day01,day02,day03".format(self.course))


cap = Campus("BJ", "Python", "三期")
cap.course_info()
cap1 = Campus("CD", "Linux", "一期")


class User():
    def __init__(self, name, age, role):
        # self.teacher = []
        #  self.student = []
        self.name = name
        self.age = age
        self.role = role


stu_num = 00


class Student(User):

    def __init__(self, name, age, role, cap):
        User.__init__(self, name, age, role)
        global stu_num
        stu_num += 1
        # zfill的用法：当字符不足两位数时，强制补充为两位，默认为0，且只能对字符串使用
        stu_id = cap.school_name + 'S' + str(stu_num).zfill(2)
        #  stu = self.student.append(name)
        self.mark_list = {}

        print("欢迎{0}同学的加入！,你的编号是{1}".format(name, stu_id))

    def stu_info(self, course):
        print("我是学员{0},我报的课程是{1}{2}".format(self.name, course.course, course.code))

    def look(self):
        for i in self.mark_list.items():
            print(i)


# 声明成全局变量是因为每次新建用户时编号都要+1，如果声明在类中创建实例时，该值永远都是1，不会增加
tea_num = 00


class Teacher(User):

    def __init__(self, name, age, role, cap):
        User.__init__(self, name, age, role)
        global tea_num
        tea_num += 1
        # zfill的用法：当字符不足两位数时，强制补充为两位，默认为0，且只能对字符串使用
        tea_id = cap.school_name + 'T' + str(tea_num).zfill(2)
        # tea = self.teacher.append(name)

        print("欢迎{0}老师的加入！,你的编号是{1}".format(name, tea_id))

    def tea_info(self, course):
        print("大家好，我是{0}老师，我教的是{1}{2}课程".format(self.name, course.course, course.code))

    def work(self, date, mark, obj):
        # print(stu.mark_list)
        # 集合添加值的操作:集合.['键'] = 值
        obj.mark_list["Day" + date] = mark


# 这里注意cap是对象，把对象当做参数传入，可以调用对象的成员属性
# 注意调用的顺序问题
tea = Teacher("小周", 100, "teacher", cap)
stu = Student("小高", 26, "student", cap)
stu1 = Student("小王", 31, "student", cap)
tea.tea_info(cap)
tea.work('2', 'A', stu)
tea.work('2', 'B', stu1)
stu.stu_info(cap)
stu.look()
stu1.look()

# tea.work(stu1,'B')
