# 游戏编程：按一下要求定义一个乌龟类和鱼类并尝试编程
# 假设游戏场景为范围(x,y)为 0<=x<=10,0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 他们的移动方向均随机
# 乌龟的最大移动能力是2（乌龟可以随机选择移动是1还是2），鱼的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼不计算体力
# 当乌龟体力值为0或者鱼的数量为0时，游戏结束

# 因为乌龟和鱼都是随机移动
# 所以导入random(随机)模块，并重命名为r
import random as r


class Tortoise():
    def __init__(self):

        # 初始化乌龟的位置
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        self.strength = 100

    def move(self):
        # 移动距离为负数代表可以往反方向移动

        new_x = r.choice([1, 2, -1, -2]) + self.x
        new_y = r.choice([1, 2, -1, -2]) + self.y

        if new_x < 0:
            self.x = 0 - new_x
        if new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        if new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.strength -= 1

        return (self.x, self.y)

    def eat(self):
        self.strength += 20
        if self.strength >= 100:
            self.strength = 100


class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = r.choice([1, -1]) + self.x
        new_y = r.choice([1, -1]) + self.y

        if new_x < 0:
            self.x = 0 - new_x
        if new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        if new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)


tortoise = Tortoise()

# 因为有十条鱼且每条鱼的位置都随机，则需要把每条鱼的位置都遍历出来，并添加到列表里
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while 1:

    tor = tortoise.move()

    # 在迭代器中直接删除列表元素很危险，因为迭代器是直接引用列表元素数据做操作(传址)
    # 所以把列表拷贝一份传给迭代器，再对原列表进行操作
    for each_fish in fish[:]:
        # 这里用.move()方法是因为fish列表里本身存的就是对象
        if each_fish.move() == tor:
            tortoise.eat()
            print("有一条鱼被吃掉了{0}".format(each_fish.move()))
            fish.remove(each_fish)

    # if x is not None`是最好的写法，清晰，不会出现错误，以后坚持使用这种写法。
    # 使用if not x这种写法的前提是：必须清楚x等于None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()时对你的判断没有影响才行

    if not len(fish):
        print("鱼被吃完了，游戏结束")
        break

    if tortoise.strength == 0:
        print("乌龟体力耗尽，游戏结束")
        break

