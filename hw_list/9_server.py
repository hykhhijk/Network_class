import socket
import threading
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)


client_list=[]

def read(sock):
    while True:
        msg = sock.recv(1024)
        msg = msg.decode()
        print(msg)
        if msg=="quit":
            print("Close ", sock)
            sock.close()
            client_list.remove(sock)
            return 
        else:
            for i in client_list:
                if i != sock:
                    i.send(msg.encode())


client_list.append(s)
while True:
    r_sock, w_sock, e_sock = select.select(client_list, [], [])
    for sock in r_sock:
        if sock == s:
            client, addr = s.accept()
            client_list.append(client)
            print("Client {} connected!".format(addr))
        else:
            msg = sock.recv(1024)
            if not msg:
                sock.close()
                client_list.remove(sock)
                continue
            else:
                for client in client_list:
                    if sock != client and client != s:
                        print(sock, s)
                        client.send(msg)


    
