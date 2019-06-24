'''
接收到客户端发送的请求头，并返回响应内容
'''
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("建立通信.......")

sock.bind(("127.0.0.1",6789))
print("绑定ip.........")

#监听
sock.listen()
print("正在监听..........")


skt,addr = sock.accept()
print("接收请求.......")
# rsp_content = "hahhahaha"
# 返回一个html页面
file_path = ".\index.html"
with open(file_path, "r", encoding="UTF-8") as f:
    # read:读取整个文件
    # readline:读取下一行
    # readlines:读取整个文件到迭代器，以供遍历
    rsp_content = f.read()

rsp_1 = "HTTP/1.1 200 OK\r\n"
rsp_2 = "Content-Length:{0}\r\n".format(len(rsp_content))
rsp_3 = "date:2019-06-04 14:09:00\r\n"
rsp_4 = "\r\n"
rsp = rsp_1 + rsp_2 + rsp_3 + rsp_4 + rsp_content
skt.send(rsp.encode())
print("发送响应..........")
skt.close()
sock.close()