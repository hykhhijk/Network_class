import socket
import threading



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 9000)
sock.connect(addr)


def read(conn):
    while True:
        msg = conn.recv(1024)
        msg = msg.decode()
        print(msg)



name = input("아이디 입력: ")
sock.send(name.encode())
th = threading.Thread(target=read, args=(sock, ))
th.start()
while True:
    msg = input("메시지를 입력: ")
    message = name+ ": " +msg
    sock.send(message.encode() )