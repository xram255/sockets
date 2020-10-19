import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

s.send(bytes("Hello from the other side..!", "utf-8"))
msg = s.recv(1024)
print(msg.decode('utf-8'))