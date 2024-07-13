#!/usr/bin/python3
import threading
import socket
import signal
import sys
host="127.0.0.1"
port=55555

#conection

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

# vars

clients =[]
nicknames = []

# establish conection

def broadcast(message):
    for client in clients:
        client.send(message)

# start in chat
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode("ascii"))
            nicknames.remove(nickname)
            break
# create a connection with a client
def receive():
    while True:
        client, address = server.accept()
        print(f"Connect with {str(address)}")

        client.send("Nick".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined to the chat".encode("ascii"))
        client.send("Connect to Sender".encode("ascii"))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()
# exit
def signal_handler(signal, frame):
    print("exiting")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("server is listening ....")
    receive()
