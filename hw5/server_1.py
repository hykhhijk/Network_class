import socket
import random
import sys
import time

BUF_SIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 5555))
sock.listen(10)
conn, addr = sock.accept()

while True:
    msg = conn.recv(BUF_SIZE)
    if msg.decode() == "Request":
        conn.send(str(random.randint(0, 40)).encode())
        temp=conn.recv(BUF_SIZE)
        conn.send(str(random.randint(0, 100)).encode())
        temp=conn.recv(BUF_SIZE)
        conn.send(str(random.randint(70, 150)).encode())
    elif msg.decode() == "quit":
        conn.close()
        sys.exit()


