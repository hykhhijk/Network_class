import socket

BUF_SIZE = 1024
port =5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("localhost", port))

while True:
    msg = input("Input message to send: ")
    if msg[0:4]=="send":
        sock.sendto(msg.encode(), ("localhost", port))
        msg, addr = sock.recvfrom(BUF_SIZE)
        print(msg.decode())
    elif msg[0:7] == "receive":
        sock.sendto(msg.encode(), ("localhost", port))
        msg, addr = sock.recvfrom(BUF_SIZE)
        print(msg.decode())
    elif msg == "quit":
        sock.sendto(msg.encode(), ("localhost", port))
        sock.close()
        break
