###### TCP client

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",5000))                #localhost는 필수이다
msg = "text"
msg = msg.encode()
sock.send()

##### TCP server

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 5000))
sock.listen(5)
conn, addr = sock.accept()
msg = conn.recv(1024)
msg = msg.decode()
print(msg)



##### Endian encode, decode(2)

##Client
msg = 1234
msg.to_bytes(4, "big")          #크기는 무조건 변환하는 자료형보다 커야함
                                #Endian은 big고정 얘네가 통신 전용임
##Server
msg = conn.recv(1024)
msg = int.from_bytes(msg, "big")


###### HTTP통신서버(4)

msg = conn.recv(1024)
msg = msg.decode()
msg_list = msg.split("\r\n")                    #요청을 줄 단위로 split
msg_send = msg_list[0].split(" ")               #첫 요청을 공백 단위로 split
if msg_send[1] == "/index.html":                #두번째 split 값이 /index.html과 같은 요청 형태임
    conn.send("HTTP/1.1 200 OK\r\n".encode())
    conn.send("Content-Type: text/html \r\n\r\n".encode())  #두줄 기본적으로 보내고
    f = open("../hw4/index.html", "r", encoding="utf-8")    #파일은 이딴식으로 가져온다음
    data = f.read()
    conn.send(data.encode("euc-kr"))                        #html 송신시에는 인코딩을 주의해야 한다.
############ html외 기타 형식은 hw4를 참고할 것



###### UDP server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 5555))
msg,addr = sock.recvfrom(1024)
sock.sendto("msg".encode(), addr)

##### UDP client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Input message: ")
sock.sendto(msg.encode(), ("localhost", 5555))
msg, addr = sock.recvfrom(1024)


##### Thread
import threading
def echoTask(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print('Received message:', data.decode())
        sock.send(data)
    sock.close()
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Thread(target=echoTask, args=(conn,))
    th.daemon=True                                          #메인 프로세스 종료시 같이 종료
    th.start()                                              #thread 등록
    th.join()                                               #메인 프로세스가 thead 종료까지 대기