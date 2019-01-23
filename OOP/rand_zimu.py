'''
打印字母游戏
'''

class GameZimu():
    # 用*号打印出字母A
    #     *
    #   *   *
    #  *      *
    # * *  * *  *
    #*            *
    def a():
        for i in range(1,7):
            for m in range(1,7-i):
                print(" ",end=" ")
            for j in range(7-i,7):
                if i == 1 or i == 4 or j == 6 or j == 7-i:
                    print("* ",end="  ")
                else:
                    print("",end="    ")

            print()

    # 用*号打印字母D
    def d():
        for i in range(1,6):
            for j in range(1,6):
                # 第一行和第五行的最后一颗星不打印
                if i == 1 or i == 5:
                    if j < 5:
                        print("*",end=" ")
                elif j == 1 or j == 5:
                    print("*",end="")
                else:
                    print(" ",end=" ")

            print()


    # 用*打印字母B，原理同上，打印两遍即可
    def b():
        for i in range(1, 5):
            for j in range(1, 6):
                # 第一行和第五行的最后一颗星不打印
                if i == 1 or i == 5:
                    if j < 5:
                        print("*", end=" ")
                elif j == 1 or j == 5:
                    print("*", end="")
                else:
                    print(" ", end=" ")

            print()
        for i in range(1, 6):
            for j in range(1, 6):
                # 第一行和第五行的最后一颗星不打印
                if i == 1 or i == 5:
                    if j < 5:
                        print("*", end=" ")
                elif j == 1 or j == 5:
                    print("*", end="")
                else:
                    print(" ", end=" ")

            print()

    def c():
        # 打印字母C
        for i in range(1, 6):
            for j in range(1, 5):
                if i == 1 or i == 5:
                    if j == 1:
                        print(" ", end="")
                    else:
                        print("* ", end="")
                elif j == 1:
                    print("*", end="")

            print()

    def k():
        # 打印字母K
        for i in range(1, 6):
            for j in range(1, 5):
                if j == 1:
                    print("* ", end="")
                elif i <= 3 and j == 5 - i:
                    print("* ", end="")
                elif i > 3 and j == i - 1:
                    print("* ", end="")
                else:
                    print(" ", end="")
            print()

zimu = GameZimu()
