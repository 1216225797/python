'''
client端流程：
    1.建立通信的socket
    2.发送内容到指定服务器
    3.接收服务器给定的反馈内容
'''

import socket

# 模拟客户端
def clientFunc():

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "哈喽啊，你吃了没？"

    # 发送的内容必须是bytes类型
    data = text.encode()

    sender = ("127.0.0.1",8080)
    sock.sendto(data,sender)

    # 返回类型由数据和地址组成，是个tuple类型
    rev_data,addr = sock.recvfrom(200)

    # 解码
    rev_data_1 = rev_data.decode()

    print(rev_data_1)

if __name__ == '__main__':
        clientFunc()

