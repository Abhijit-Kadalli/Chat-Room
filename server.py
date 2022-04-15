import socket  
import threading

# GLOBAL CONSTANTS IN CAPS
FORMAT = "utf-8"
HEADER = 64
PORT = 5500
SERVER = socket.gethostbyname(socket.gethostname()) # SERVER = "192.168.0.104" or use the line below to save the hassle
ADDR = (SERVER,PORT)
DISSCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# handles all the communication between the client and server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISSCONNECT_MESSAGE:
                connected = False 
            
            print(f"[{addr}]: {msg}")
        
    conn.close()



# new connection handling part
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER} ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() -1}")

print("[STARTING]  Server is starting...")    
start()