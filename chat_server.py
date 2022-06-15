from email import message
import socket as sc

s = sc.socket()
s.bind(('localhost',8080))
s.listen()
conn,adr = s.accept()
conn.send(bytes('Sagnik server','UTF-8'))
name = conn.recv(1024).decode()
print(name+" entered the chat")
while True:
    message = input("Me: ")
    if(message == "Bye"):
        conn.send(bytes("Left the chat",'UTF-8'))
        print("\n")
        break
    conn.send(bytes(message,'UTF-8'))
    print(name + ": " + conn.recv(1024).decode())


