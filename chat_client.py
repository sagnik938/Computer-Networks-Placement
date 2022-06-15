import socket as sc

c = sc.socket()
c.connect(('localhost',8080))
c.send(bytes('Sagnik client','UTF-8'))
name = c.recv(1024).decode()
print(name+" entered the chat")
while(True):
    print(name + ": " + c.recv(1024).decode())
    message = input("Me: ")
    if(message == "Bye"):
        c.send(bytes("Left the chat",'UTF-8'))
        c.close()
        print("\n")
        break
    c.send(bytes(message,'UTF-8'))

