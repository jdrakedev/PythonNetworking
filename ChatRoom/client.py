# Chat Room Connection - Client To Client

import threading 
import socket

# get an alias
alias = input("Choose an alias: ")
# create a client object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# instead of binding a client to a host and a board we're going to connect it 
client.connect(("127.0.0.1", 59000)) # connect client to the localhost, and our port

# now we will create two functions for two threads:
# 1. for recieving messages from other clients through the server
# 2. to send messages to other clients also through the server 

# NOTE: encode runs with send, decode runs with recieve

def client_recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8") # we decode because we are recieving and not sending
            if message == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(message) # recieved from the server
        except:
            print("Error!")
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode("utf-8"))

recieve_thread = threading.Thread(target = client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()



