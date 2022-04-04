import socket
import sys
import time

BUF_SIZE = 1024

sock_1_addr = 5555
sock_2_addr = 6666
sock_1=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_2=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_1.connect(("localhost", sock_1_addr))
sock_2.connect(("localhost", sock_2_addr))
f = open("./data.txt", "a")
while True:
    msg = input("Input number of device for request data: ")

    if msg=="1":
        sock_1.send("Request".encode())
        data_1 = sock_1.recv(BUF_SIZE)
        sock_1.send("done".encode())
        data_2 = sock_1.recv(BUF_SIZE)
        sock_1.send("done".encode())
        data_3 = sock_1.recv(BUF_SIZE)
        t = time.asctime()
        output = t+': Device1: Temp='+ data_1.decode()+ ', Humid='+ data_2.decode()+ ', Illum='+ data_3.decode()+ '\n'
        output = str(output)
        print(output)
        f.write(output)
        # print(data_1.decode(), data_2.decode(),data_3.decode())


    elif msg=="2":
        sock_2.send("Request".encode())
        data_1 = sock_2.recv(BUF_SIZE)
        sock_2.send("done".encode())
        data_2 = sock_2.recv(BUF_SIZE)
        sock_2.send("done".encode())
        data_3 = sock_2.recv(BUF_SIZE)
        t = time.asctime()
        output = t+': Device2: Heartbeat='+ data_1.decode()+ ', Steps='+ data_2.decode()+ ', Cal='+ data_3.decode()+ '\n'
        output = str(output)
        print(output)
        f.write(output)
        # print(data_1.decode(), data_2.decode(),data_3.decode())

    elif msg=="quit":
        sock_1.send("quit".encode())
        sock_2.send("quit".encode())
        sock_1.close()
        sock_2.close()
        sys.exit()