import socket
from multiprocessing import TimeoutError

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)

print(s)

for _ in range(3):
    print("runing")
    clientsocket, address = s.accept()
    data = clientsocket.recv(1024)
    print(data.decode('utf-8'))
  
        
    print(f"Connection from {address} has been established ")
    clientsocket.send(bytes("Welcome to the server ", "utf-8"))
    clientsocket.close()
    
print("closed")