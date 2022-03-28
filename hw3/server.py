import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9000))
s.listen(2)
while True:
    client, addr = s.accept()
    print("Connection from ", addr)
    while True:
        formula = client.recv(1024).decode()
        answer=0
        if not formula:
            break
        elif formula.find("+") != -1:
            index = formula.find("+")
            answer = str(int(formula[:index].strip()) + int(formula[index+1:].strip()))
        elif formula.find("-") != -1:
            index = formula.find("-")
            answer = str(int(formula[:index].strip()) - int(formula[index+1:].strip()))
        elif formula.find("*") != -1:
            index = formula.find("*")
            answer = str(int(formula[:index].strip()) * int(formula[index+1:].strip()))
        elif formula.find("/") != -1:
            index = formula.find("/")
            answer = str(round(int(formula[:index].strip()) / int(formula[index+1:].strip()), 1))
        else:
            answer = "Input error"
        client.send(answer.encode())
    client.close()