import selectors
import socket

sel = selectors.DefaultSelector()


def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    print("Recieved data: ", data.decode())
    # conn.send(data)


sock_1 = socket.socket()
sock_2 = socket.socket()
sock_1=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_2=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_1.connect(("localhost", 5555))
sock_2.connect(("localhost", 6666))
sock_1.send("Register".encode())
sock_2.send("Register".encode())


sel.register(sock_1, selectors.EVENT_READ, read)
sel.register(sock_2, selectors.EVENT_READ, read)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data                 #selector에 인수로 넘긴 callback func
        callback(key.fileobj, mask)         #읽을게 있는 소켓

