import socket
import time
sock = socket.socket()
sock.bind(("", 6666))
sock.listen()

conn, addr = sock.accept()
while True:
    msg = conn.recv(1024)
    msg = msg.decode()
    if msg == "Register":
        while True:
            time.sleep(1)
            conn.send("temp".encode())