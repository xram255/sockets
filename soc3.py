import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "djxmmx.net"
port = 17
#server_ip = socket.gethostbyname(server)
#print(server_ip)

request = "GET / HTTP/1.1\r\nHost: " + server + " \r\n\r\n"

s.connect((server, port))
s.send(request.encode())

result = s.recv(4096)

print(result.decode('utf-8'))