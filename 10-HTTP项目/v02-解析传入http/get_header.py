'''
目标：
获取到客户端的请求头，并按照字典的格式打印出来


b = b''         # 创建一个空的bytes
b = bytes()      # 创建一个空的bytes
b = b'hello'    #  直接指定这个hello是bytes类型
b = bytes('string',encoding='编码类型')  #利用内置bytes方法，将字符串转换为指定编码的bytes
b = str.encode('编码类型')   # 利用字符串的encode方法编码成bytes，默认为utf-8类型

bytes.decode('编码类型')：将bytes对象解码成字符串，默认使用utf-8进行解码。
'''

import socket

def read_line(skt):
    # 定义两个变量读取字节格式的请求头，b1一个一个的往前读取，
    # 然后再把b1的值赋值给b2,当b1读取到\n，b2读取到\r时则停止，
    # 最后再把获取到值赋值给一个参数，此为一行
    b1 = skt.recv(1)
    b2 = 0
    data = b''
    # 当b1读取到\n,并且b2读取到\r，则说明读到换行符，改行读取完成
    # 注意：\r和\n也要是byte格式

    # split()和strip()的区别：
    # split：按照指定的字符分割字符串返回列表类型
    # strip：去除首尾指定的字符
    while b1 != b'\n' and b2 != b'\r':
        b2 = b1
        b1 = skt.recv(1)
        # 强制转换为bytes类型
        data += bytes(b2)
    # 解码成编码为UTF-8的字符串格式
    return data.strip(b'\r').decode()

def get_headers(skt):
    # 声明一个字典来存在结果
    dic = dict()
    line = read_line(skt)
    # 请求头和实体之间有空行，当读取到空行即读不到内容时，表示内容读取完成
    while line:
        # 判断两种情况：
        # 1.当分隔符为"："，说明是请求头，则直接获取键值
        # 2.否则说明是首部行，以空格为分隔符获取值添加建

        # 使用split注意，分割的字符串是以列表的形式存储
        # 当返回两部分时则说明是请求头，反之则说明是首部行
        msg = line.split(r": ")
        if len(msg) == 2:
            # 字典添加键值
            dic[msg[0]] = msg[1]
        else:
            msg2 = line.split(r" ")
            dic["method"] = msg2[0]
            dic["address"] = msg2[1]
            dic["version"] = msg2[2]
        # print(line)
        line = read_line(skt)
    return dic


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定
sock.bind(("127.0.0.1",9080))

# 监听
sock.listen()

# 接收通信socket,接收两个值
skt,addr = sock.accept()
print("接收socket....")

# 接收消息
# msg = skt.recv(500)
# print(msg)
print(get_headers(skt))

skt.close()
sock.close()
