'''
以面向对象的形式，把tcp的两个socket，即WebServer(初始建立的socket)
和SocketHandle(真正通信用的socket)分成两个对象来实现

实现步骤：
1.WebServer：建立初始socket
2.Sockethandle:
    i.截取客户端发送过来的请求头，并保存到字典中
    ii.返回响应头信息
'''
import socket
import header_config as hc

class SocketHandle():
    def __init__(self,skt):
        self.skt = skt

    def getLine(self):
        b1 = self.skt.recv(1)
        b2 = 0
        # 申请一个字节类型的空字符串，用来存放接收的符合条件的字符
        msg = b''
        while b1 != b"\n" and b2 != b"\r":
            b2 = b1
            b1 = self.skt.recv(1)
            msg = msg + bytes(b2)
        return msg.strip(b'\r').decode()

    def getHeader(self):
        '''
        获取头部所有信息

        以"："为分隔符
        1.当存在此分隔符，则为请求头信息，获取键值
        2.否则为首部行信息，添加键
        :return:
        '''
        # 声明一个字典用来以键值对的形式保存所有请求头的信息
        self.data = {}
        line = self.getLine()
        while line:
            # split截取之后以列表的形式返回

            # 如果截取到了两部分，则说明是请求头信息
            if len(line.split(r": ")) == 2:
                self.data[line.split(": ")[0]] = line.split(": ")[1]
            # 否则是首部行信息
            else:
                data_head = line.split(r" ")
                self.data["method"] = data_head[0]
                self.data["uri"] = data_head[1]
                self.data["version"] = data_head[2]
            line = self.getLine()
        return self.data


    def readFile(self,url):
        '''
        UTF-8编码下一个汉字或者中文标点符号占用三个字节，
        如果用普通"r"模式读取文件，则不管是汉字还是字母都是按照一个字符来读取，
        但是content-length时按照字节数来读取文件内容，所以，在读取文件内容的时候，
        要用"b"模式(二进制模式)读取。
        :return:
        '''
        with open(url, "rb") as f:
            self.ff = f.read()
            self.sendRsp(self.ff)
            print(len(self.ff))
        return self.ff

    # 添加路由信息
    def rspRoute(self):
        uri = self.data.get("uri")
        # 获取到的uri为二进制
        if uri == "/":
            print(uri)
            self.readFile(r".\static\index.html")
        if uri == "/favicon.ico":
            self.readFile(r".\static\fav.jfif")
        self.readFile(r".\static\404.html")

    def sendRsp(self, msg):
        rsp_1 = hc.Config.state + "\r\n"
        rsp_2 = "Content-Length:" + str(len(msg)) + "\r\n"
        rsp_3 = "date:" + hc.Config.date + "\r\n"
        # 注意:
        # "\r\n"这行必须写，且content内容在"\r\n"(即空行后)，按照该格式写
        # 不然识别不出来
        rsp_4 = "\r\n"
        rsp_content = msg

        # rsp = rsp_1 + rsp_2 + rsp_3 + rsp_4 + rsp_content
        self.skt.send(rsp_1.encode())
        self.skt.send(rsp_2.encode())
        self.skt.send(rsp_3.encode())
        self.skt.send(rsp_4.encode())
        self.skt.send(rsp_content)
        # print(rsp)

    def main(self):
        print(self.getHeader())
        self.rspRoute()

class WebServer():
    def __init__(self,ip=hc.Config.ip,port=hc.Config.port):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # bind()函数传入的是个元组
        self.sock.bind((self.ip, self.port))
        print("IP已绑定.......")
        self.sock.listen()
        print("已开启监听.......")
    def start(self):
        '''
        服务端提供不间断永久性服务

        只要监听到请求，就把请求移交给SocketHandle处理，然后关闭当前skt
        :param sock:
        :return:
        '''
        while True:
            skt,addr = self.sock.accept()
            if skt:
                # 实例化对象
                socketHandle = SocketHandle(skt)
                socketHandle.main()
                # print("执行完毕......")
                skt.close()

if __name__ == '__main__':
    ws = WebServer()
    ws.start()