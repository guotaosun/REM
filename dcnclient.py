# install ws4py# pip install ws4py# easy_install ws4pyfrom ws4py.client.threadedclient import WebSocketClientclass DummyClient(WebSocketClient):
import socket
#创建一个客户端的socket对象
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #设置服务端的ip地址
# host = "127.0.0.1"
# #设置端口
# port = 9999
# #连接服务端
# client.connect((host, port))
#
# #while循环是为了保证能持续进行对话
# while True:
#     #输入发送的消息
#     sendmsg = input("请输入:")
#     #如果客户端输入的是q，则停止对话并且退出程序
#     if sendmsg=='q':
#         break
#     sendmsg = sendmsg
#     #发送数据，以二进制的形式发送数据，所以需要进行编码
#     client.send(sendmsg.encode("utf-8"))
#     msg = client.recv(1024)
#     #接收服务端返回的数据，需要解码
#     print(msg.decode("utf-8"))
# #关闭客户端
# client.close()

import socket
import time

class DCNClient:
    def __init__(self, username, port):
         self.username = username
         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         self.socket.connect(("127.0.0.1", port))

    def send_msg(self, msg):
        self.socket.send("{username}::{msg}".format(username=self.username,msg=msg).encode("utf-8"))

    def recv_msg(self):
        data=self.socket.recv(1024)
        if data:
            print("\n【自动化云端测试系统】"+" "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
            print(data.decode("utf-8"))
            return True
        return False

    def main(self):
        data = self.socket.recv(1024)
        print(data.decode("utf-8"))
        msg = input("请输入消息：")
        self.send_msg(msg)
        while True:
            if self.recv_msg():
                msg=input("\n我：")
                self.send_msg(msg)
                if msg == "exit":
                    print("对话已关闭")
                    break

if __name__ == '__main__':
    cc = DCNClient(username="孙国涛", port=9999)
    cc.main()