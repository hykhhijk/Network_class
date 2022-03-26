import socket

s = socket.socket()
s.bind(("",80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split("\r\n")
    print(req)
    req_msg = req[0].split()[1]
    if req_msg=="/index.html":
        c.send("HTTP/1.1 200 OK\r\n".encode())
        c.send("Content-Type: text/html \r\n\r\n".encode())
        f = open("index.html", "r", encoding="utf-8")
        data = f.read()
        c.send(data.encode("euc-kr"))
    elif req_msg=="/iot.png":
        c.send("HTTP/1.1 200 OK\r\n".encode())
        c.send("Content-Type: image/png \r\n\r\n".encode())
        f = open("iot.png", "rb")
        data = f.read()
        c.send(data)
    else:
        c.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        c.send("<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>".encode())
        c.send("<BODY>Not Found</BODY></HTML>".encode())
        break


        


    c.close()