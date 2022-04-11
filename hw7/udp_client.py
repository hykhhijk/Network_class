from random import random
import socket
import random
import time


port = 3333
BUFF_SIZE = 1024
addr = ("localhost", port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    while True:
        reTx = 0
        msg = input("-> ")
        while reTx <= 3:
            resp = str(reTx) + " " + msg
            sock.sendto(resp.encode(), addr)
            sock.settimeout(2)

            try:
                data, addr = sock.recvfrom(BUFF_SIZE)
            except socket.timeout:
                reTx += 1
                continue
            else:
                break
        if reTx==4:
            print("Try resend!")
            continue
        else:
            break        


    while True:
        sock.settimeout(None)
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b"ack", addr)
            print("<- ", data.decode())
            break
        
