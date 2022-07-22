#!/usr/bin/python3
import socket
import threading
import signal
import sys

nickname = input("Choose a Nickname: ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55555))

def signal_handler(sig, frame):
    print("\n\n[*] Exiting...\n")
    sys.exit(0)

# handle exiting
signal.signal(signal.SIGINT, signal_handler)


# starting the connection
def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "Nick":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("An error ocurred")
            client.close()    
            break

# sending messages
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

if __name__ == "__main__":
    
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
