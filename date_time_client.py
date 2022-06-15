import socket as sc

c = sc.socket()
c.connect(('Localhost',8080))
print(c.recv(1024).decode())