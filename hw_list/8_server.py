import socket
import threading

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



while True:
    client, addr = s.accept()

    if client not in client_list:
        client_list.append(client)
        print("New client", addr)
        th = threading.Thread(target = read, args=(client,))
        print("Thread start!")
        th.start()

    
