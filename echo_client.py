import socket as sc
c = sc.socket()
c.connect(('localhost',8080))
c.send(bytes('Hi Server','UTF-8'))
print(c.recv(1024).decode())