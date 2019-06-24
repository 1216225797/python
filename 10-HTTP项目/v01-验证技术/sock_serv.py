'''
该验证以浏览器为客户端，通过ip+端口的形式访问服务端
验证客户端与服务端之间SOCKET_TCP协议通信是否畅通
'''
# 导入socket包
import socket

# 创建socket
# AF_INET:IVP4协议族
# SOCK_STREAM:TCP协议
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址，包含IP和端口，元组类型
sock.bind(("127.0.0.1",8080))

# 添加监听
sock.listen()

# 接收监听到的socket，元组类型，两个参数分别是socket和地址
skt,addr = sock.accept()
print(type(skt))
print(type(addr))
print(skt)
print(addr)
# 接收发送过来的内容,一定要有缓存区
# 内容是客户端的请求头
msg = skt.recv(200)
print(type(msg))
print(msg)

# 解码，默认UTF-8，可以指定其他的编码格式，但是解码和编码格式要一致
text = msg.decode()
print(type(text))
print(text)

# 给客户端一个返回消息
re_msg = "又下雨了，好烦呀"

# 发送
skt.send(re_msg.encode())
print("返回消息已发送、、、、")

# 关闭socket
skt.close()
sock.close()
print("end......")