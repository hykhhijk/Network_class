import socket
import random
import sys

BUF_SIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 6666))
sock.listen(10)
conn, addr = sock.accept()

while True:
    msg = conn.recv(BUF_SIZE)
    if msg.decode() == "Request":
        conn.send(str(random.randint(40, 140)).encode())
        temp=conn.recv(BUF_SIZE)
        conn.send(str(random.randint(2000, 6000)).encode())
        temp=conn.recv(BUF_SIZE)
        conn.send(str(random.randint(1000, 4000)).encode())

    elif msg.decode() == "quit":
        conn.close()
        sys.exit()



