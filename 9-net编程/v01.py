'''
server端流程：
1.建立socket，socket是负责具体通信的一个实例
2.绑定，为创建的socket指派固定的端口和ip地址
3.接收对方发送内容
4.给对方发送反馈，此步骤为非必须步骤
'''

import socket

# 模拟服务器端函数
def serverFunc():
    # 建立socket
    # socket.AF_INET：使用ivp4协议族
    # socket.SOCK_DGRAM：使用UDP通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定ip和port
    sock.bind(("127.0.0.1",8080))

    # 接收对方消息
    # 参数的含义是缓存区的大小
    data,addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    # 发送过来的数据是bytes格式，所以要进行解码操作
    text = data.decode()
    print(text)
    print(type(text))

    # 返回给客户端的消息
    data_1 = "我是返回的消息呀"
    rsp = data_1.encode()
    # send和sendto的区别:sendto用作UDP协议
    sock.sendto(rsp,addr)

if __name__ == '__main__':
    print("start....")
    serverFunc()
    print("end.....")