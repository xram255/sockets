import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)

print(s)

while True:
    print("runing")
    clientsocket, address = s.accept()
    print(clientsocket)
    print(f"Connection from {address} has been established ")
    clientsocket.send(bytes("Welcome to the server ", "utf-8"))
    clientsocket.close()
    