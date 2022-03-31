import socket
import sys

BUF_SIZE = 1024

sock_1_addr = 5555
sock_2_addr = 6666

while True:
    sock=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    msg = input("Input number of device for request data: ")

    if msg=="1":
        sock.connect(("localhost", sock_1_addr))
        sock.send("Request".encode())
        data_1 = sock.recv(BUF_SIZE)
        sock.send("done".encode())
        data_2 = sock.recv(BUF_SIZE)
        sock.send("done".encode())
        data_3 = sock.recv(BUF_SIZE)
        print(data_1.decode(), data_2.decode(),data_3.decode())

    elif msg=="2":
        sock.connect(("localhost", sock_2_addr))
        sock.send("Request".encode())
        data_1 = sock.recv(BUF_SIZE)
        sock.send("done".encode())
        data_2 = sock.recv(BUF_SIZE)
        sock.send("done".encode())
        data_3 = sock.recv(BUF_SIZE)
        print(data_1.decode(), data_2.decode(),data_3.decode())

    elif msg=="quit":
        sock.connect(("localhost", sock_2_addr))
        sock.send("quit".encode())
        sock.close()
        sys.exit()
    sock.close()
