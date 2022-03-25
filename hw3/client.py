import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 9000)
sock.connect(addr)

while True:
    formula = input("Input formula: ")
    if formula == "q":
        break
    sock.send(formula.encode())
    print(sock.recv(1024).decode())

sock.close()      