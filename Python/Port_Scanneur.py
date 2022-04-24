import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP à test :")
port = 1

def portscanneur(port):
    for port in range(1, 65535):
        if sock.connect((host,port)):
            print ("Port fermer :" % (port))
            port = port + 1
        else:
            print ("Port ouvert :" % (port))
            port = port + 1

portscanneur(port)
