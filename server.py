import socket  
import threading
import sys
import time

s = socket.socket()
print("socket was successfully created")

port = 12345
s.bind("", port)
print("The socket binded to %s" %(port))

s.listen(5)

while True:
    c, addrs = s.accept()
    print("got connection from ", addrs)
    c.send("Thank you, you have successfully connected to the server")
    c.close()
    break
