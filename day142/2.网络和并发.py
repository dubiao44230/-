#!/usr/bin/env python
"""

"""
# 1. 简述OSI 7层模型。


# 2. TCP 三次握手 和 四次挥手。


# 3. TCP和UDP区别？


# 4. 黏包显现
"""
    缓冲区 + 连续发送数据
    struct模块实现数据封包：头(数据长度)+数据
"""


# 5. B/S和C/S架构
"""
    B/S, 写网站
    C/S, 写软件（Java、C++）
"""

# 6. Http协议
"""
    - 基于TCP协议实现
    - 一次请求一次响应后断开连接。
    - 格式：
        请求
            - 请求头
                - user-agent，告诉服务器我的设备信息。
                - accept,告诉服务器我能接受返回数据的格式。
                - content-type,告诉服务器我发送的请求体的格式（数据类型）
                - cookies，浏览器端的cookie信息。
                - host，主机信息
                - Connection,值keepalive，告诉服务器保持连接状态。
                - referer,将浏览器上一次访问的地址发送给服务器（可以做图片防盗链）。
                - 请求方法：GET/POST/DELETE/PUT/PATCH/OPTIONS    
            - 请求体
            
            "GET /yuanchenqi/articles/9993188.html http1.1\r\nuser-agent:k1\r\nhost:cnblogs.com...\r\n\r\n"
            "POST /yuanchenqi/articles/9993188.html http1.1\r\nuser-agent:k1\r\nhost:cnblogs.com...\r\n\r\nk1=123&k2=456"
            
        响应：
            - 响应头
                - location,让用户重定向到指定url。
                - set-cookies,给用户浏览器设置cookie。
                - 状态码：
                    - 200，201、202
                    - 300
                    - 400
                    - 500
            - 响应体
                - 用户看到的内容。
        
        

"""

# 7. Websocket协议（服务器向客户端主动推送消息）
"""
    - 基于TCP实现的协议。
    - 连接之后不断开
    - 连接之后需要先进行握手
        - 获取客户端发送过来的随机字符串：在请求Sec-WebSocket-Key中获取，如：mnwFxiOlctXFN/DeMt1Amg==
        - base64.b64encode(hashlib.sha1(mnwFxiOlctXFN/DeMt1Amg== + magic string))
        - 返回给客户浏览器，在响应头中设置：Sec-WebSocket-Accept: 加密后的值
    - 握手通过后，进行收发数据（加密）：
        - 127: 2+8字节   MASK（4字节）+数据
        - 126: 2+2字节   MASK（4字节）+数据
        - 125: 2字节     MASK（4字节）+数据
    - 返回数据加密。
"""

# 8. Https
"""
"""

# 9. 进程、线程、协程区别？
"""
    进程，计算机中资源分配的最小单元。
    线程，计算机cpu调度的最小单元。一个进程中中可以创建多线线程，进程用于维护一个空间，线程则在此空间内进行工作。
    协程，在计算机中不存在，是由开发者人为创造出来的，也可以称为“微线程”。（人为控制一个线程在函数见进行切换执行），单纯的协程无法提供性能。
          协程          !=> 性能提高 
          协程 + IO切换  => 性能提高
"""

# 10. GIL锁是什么鬼？
"""
    GIL，全局解释器锁。
    GIL锁，保证一个进程中同一时刻只有一个线程可以被CPU调度。
    
    
    Python：
        计算型的操作（利用cpu）：多进程。
                      IO性操作：多线程、协程
                      
    应用：
        爬虫，进程+协程。
        
    注意：C Python中才有GIL。
    
    
        
"""
# 11. GIT锁可以保证数据安全吗？
"""
    无法保证数据安全，想要数据安全必须使用：Lock、RLock、Condition、Event...
"""

# 12. IO多路复用？
"""
    帮助开发者监听多个socket是否发生变化（连接、收发部署）。
    
        sk1 = socket.socket()
        sk1.bind((...,8001))
        sk1.listen(5)
        
        
        while True:
            # [sk1,sk2]
            # [sk2,]
            rlist,w,e = select.select([sk1,conn管松松,conn苟陇辉],[],[],0.5)
            for sk in rlist:
                if sk = sk1:
                    # 服务端socket变化，新用户来连接
                    conn,addr = sk.accept()
                    conn.send('你好')
                else:
                    # 客户端socket变化，老用户发来消息
                    data = sk.recv()
                    
    帮助开发者监听多个“IO句柄”发生变化（连接、收发部署）。
    
    实现IO多路复用：
        win:
            select
        linux:
            select， 个数最多1024个;轮询检测。
            poll，轮询检测。（水平触发）
            epoll，回调通知。（边缘触发）
    
    应用场景：
        wsgiref，socket
        uwsgi，socket+IO多路复用
        nginx，IO多路复用
    
"""























































