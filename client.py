from email import message
import socket

FORMAT = "utf-8"
HEADER = 64
PORT = 5500
DISSCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.104" # THIS GLOBAL CONSTANT WILL VARY FOR EVERYONE USE THE ONE YOU GOT IN THE server.py
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.decode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length = b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("HELLO WORLD!!") 
input()   
send("HELLO WORLD!!")  
input()
send("HELLO WORLD!!")
input()  
send(DISSCONNECT_MESSAGE)   