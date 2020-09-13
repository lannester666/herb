#建立连接，接收参数、图像数据、用HTTP协议转发
import socket,re
import urllib.request,http.client,os,time
import _thread

def prohard(conn,addr):
    # 存放django 发来的控制消息
    contro_message = "t=15.00&l=10000&p=100000&h=40.00"
    while True:
        # 存放接受的图像文本数据
        txt = b''
        img = b''
        # 存放接收的带终止符的图像文本数据
        img_end = b''
        txt_end = b''

        # 接收图像数据
        while True:
            buftmp = conn.recv(1024)
            print('image:', buftmp)
            # 图像数据结尾标志字符
            b = b''
            b += "|*graph*|".encode()
            img_end += buftmp
            if img_end.find(b) != -1:
                a = img_end.split(b)
                img += a[0]
                print("imageend")
                conn.send(("grahoicget").encode())
                break
        # 接收文本数据（环境参数）
        while True:
            tbuftmp = conn.recv(1024)
            print('text:', tbuftmp)
            # 文本数据结尾标志字符
            a = b''
            a += "|*text*|".encode()
            txt_end += tbuftmp
            if txt_end.find(a) != -1:
                print("textend")
                b = txt_end.split(a)
                txt += b[0]
                # conn.send("t=02.20&l=10005&p=101150&h=30.22".encode())
                conn.send(contro_message.encode())
                break
        # 将图片存入文件
        filename = time.strftime('%Y%m%d%H%M%S', time.localtime())
        filename += '.jpeg'
        f = open(filename, 'wb')
        f.write(img)
        f.close()
        data = {'text': txt.decode()}
        # 转发参数到django,接收django返回的控制消息
        url = 'http://localhost:8080/hard'
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        data_encode = urllib.parse.urlencode(data).encode('utf-8')
        request = urllib.request.Request(url, data_encode, headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        print("控制消息：", html)
        contro_message = html
        # 处理控制消息

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8082))
s.listen(50)
print("Server Starting")
while True:
    # 控制信息格式
    # t=2.2&l=5&p=6&h=2.2
    # l的值有三种格式：99999:开灯 99998:关灯 0-99997:光照强度
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind(('', 8082))
    #s.listen(50)
    #print("Server Starting")
    conn, addr = s.accept()
    print("connected by ", addr)
    _thread.start_new_thread(prohard,(conn,addr))
#conn.close()
s.close()
