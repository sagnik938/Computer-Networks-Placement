import socket as sc

s = sc.socket()
s.bind(('localhost',8080))
s.listen()
while(True):
    conn,addr = s.accept()
    conn.send(bytes('Hi Client','UTF-8'))
    print(conn.recv(1024).decode())