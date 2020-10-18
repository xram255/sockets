import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "terroristic-shoes.000webhostapp.com"
port = 80
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+ server + "\n\n"
#request = "GET / HTTP/1.1\nHost: "+ "httpbin.org" + "\n\n"
s.connect((server, port))
s.send(request.encode())

result = s.recv(4096)

print(result.decode('utf-8'))

