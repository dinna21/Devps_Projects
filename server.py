import socket
import threading 
import time
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# server =  "172.22.192.1"
server = socket.gethostbyname(socket.gethostname())
print(server)
print(socket.gethostname())
PORT = 5050
ADDR = (server,PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"Received: {msg} from {addr}")
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {ADDR}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Connected with {addr}")
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
print("[STARTING] Server is starting.........")
start()