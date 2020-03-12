#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py
#asyncio
# import socket  # 导入 socket 模块
#
# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 9999  # 设置端口
# s.bind((host, port))  # 绑定端口
#
# s.listen(5)  # 等待客户端连接
# while True:
#     c, addr = s.accept()  # 建立客户端连接
#     print
#     '连接地址：', addr
#     c.send('欢迎jobid！')
#     c.close()  # 关闭连接
import asyncio
import itertools
# import sys
# import time
#
# async def a():
#     print('Suspending a')
#     await asyncio.sleep(0)
#     print('Resuming a')
#
#
# async def b():
#     print('In b')
#
#
# async def main():
#     await asyncio.gather(a(), b())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# import asyncio
# import  time
# async def get_jobid(url):
#     print("start get jobid")
#     # 这是一个同步阻塞的接口，不要使用在这种协程里面
#     # time.sleep(1) ，
#     # await 后面必须是<class 'generator'>
#     await asyncio.sleep(2)
#     print("end get jobid")
#     return 'jobid  time pri'
# def callback(url,future):
#     """
#     会将furure传入进来
#     """
#     print(url)
#     print("任务完成，回调函数，发个测试结果。")
# if __name__ == "__main__":
#     a = time.time()
#     print("start____",)
#     # 创建一个事件循环对象loop
#     loop = asyncio.get_event_loop()
#     #############################################################
#     # 使用run_until_complete方法（阻塞的）
#     # loop.run_until_complete(get_html("https://www.baidu.com"))
#     #################################################################
#     # 同时并发10个
#     tasks = [get_jobid("https://www.baidu.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     #loop.run_until_complete(asyncio.gather(*tasks))
#     # 与wait的区别？ gather更加高层，除了上述功能，还可以将task任务分组
#     """
#     task1 = [get_html("https://www.baidu.com") for i in range(10)]
#     task2 = [get_html("https://alibaba.com") for i in range(10)]
#     loop.run_until_complete(asyncio.gather(*task1,*task2))
#     或者
#     taks1 = asyncio.gather(*task1)
#     taks2 = asyncio.gather(*task2)
#     task2.cancel() # 将任务取消掉
#     loop.run_until_complete(asyncio.gather(task1,task2))
#     """
#
#     print(time.time() - a)
#     print("end____")
#     ##################################################################
#     print("go go ...............")
#     # 获取返回的值
#     # 把协程提交进去
#     get_future = asyncio.ensure_future(get_jobid("https://www.baidu.com"))
#     # loopp中 task = loop.create_task() 没有多大区别
#
#     # 增加一个回调函数
#     from functools import partial # 可以将函数包装成另外一个函数
#     func = partial(callback,"www.baidu.com")
#     get_future.add_done_callback(func)
#
#
#     # 将get_future 运行完成，
#     # run_until_complete 接收的类型非常丰富，可以是get_future ，也可以是协程类型，比较灵活
#     loop.run_until_complete(get_future)
#     print(get_future.result())
import socket
import time
import threading
import requests
import json

class DCNREMServer:
     def __init__(self, port):
        # 绑定服务器的ip和端口，注意以tuple的形式
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", port))
        self.socket.listen(5)
        # 图灵机器人，授权码
        self.key = "your tuling robot key"
        print("正在监听 127.0.0.1 ：{}...".format(port))

     def tcplink(self, sock, addr):
        # 每次连接，开始聊天前，先欢迎下。
        sock.send("你好，欢迎执行自动化测试！".encode("utf-8"))
        while True:
            data = sock.recv(1024).decode("utf-8")
            print(sock.getpeername())
            print(sock.getsockname())
            print(sock.fileno())
            username = data.split("::")[0]
            msg = data.split("::")[1]
            if msg == "exit":
                break
            if msg:
                print("【"+username+"】 "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
                print(msg)
                response = self.get_response(msg)
                sock.send(response.encode("utf-8"))
        sock.close()
        print("与 {} 结束测试！".format(username))

     def get_response(self, info):
        # 调用图灵机器人API
        url = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        return jd['text']

     def main(self):
        while True:
            sock, addr = self.socket.accept()
            t=threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

if __name__ == '__main__':
    cs = DCNREMServer(port=9999)
    cs.main()