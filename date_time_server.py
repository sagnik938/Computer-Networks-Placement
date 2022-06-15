import socket as sc
import time as t

s = sc.socket()
s.bind(('Localhost',8080))
s.listen()
while(True):
    conn , addr = s.accept()
    print(conn,addr)
    curr = t.ctime(t.time())
    conn.send(bytes(str(curr),'UTF-8'))
