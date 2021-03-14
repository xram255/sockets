import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print('server runing...')
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} is established..")
    clientsocket.send(bytes("Hi...", "utf-8"))
