import socket

BUF_SIZE = 1024
port =5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

msg_dict={}

while True:
    msg, addr = sock.recvfrom(BUF_SIZE)
    msg = msg.decode()
    if msg[0:4]=="send":
        if msg.split()[1] not in msg_dict:
            msg_dict[msg.split()[1]] = []
            msg_dict[msg.split()[1]].append(" ".join(msg.split()[2:]))
        else:
            msg_dict[msg.split()[1]].append(" ".join(msg.split()[2:]))
        print(msg_dict)
        sock.sendto("OK".encode(), addr)
    elif msg[0:7] == "receive":
        if msg.split()[1] in msg_dict and len(msg_dict[msg.split()[1]]) != 0:
            msg_to_send = msg_dict[msg.split()[1]].pop(0)
            sock.sendto(msg_to_send.encode(), addr)
        else:
            sock.sendto("No messages".encode(), addr)
    elif msg == "quit":
        sock.close()
        break