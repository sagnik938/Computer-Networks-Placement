import socket as sc
import os

def getownip():
    hname = sc.gethostname()
    ip = sc.gethostbyname(hname)
    return({'ip':ip,'hostname':hname})

def getany(hostname):
    ip = sc.gethostbyname(hostname)
    resp = os.popen(f"ping {ip}").read()
    print(resp)
    return({'ip':ip,'hostname':hostname})

print(getownip())
print(getany('LAPTOP-QD7EALF2'))