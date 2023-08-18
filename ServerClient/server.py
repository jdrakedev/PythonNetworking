'''
Server Client Connection
'''

# Server Methods 
# bind() - binds to a specific ip and port (can listen to incoming requests)
# listen() - puts the server into a listen mode that can listen for incoming connections
# accept() - initiates a connection with the client 
# close() - closes the connection with the client

# recommiting to appear in contributions 

import socket

s = socket.socket()
print("Socket created succesfully")

port = 56789
# takes ip and port arguments
s.bind(('', port)) 
print(f"Socket binded to port{port}")

# 5 means 5 connections which is the limit for our server to listen to 
s.listen(5) 
print("Socket is listening")

while True:
    # c = connection, addr = address
    c, addr = s.accept() 
    print(f"Got connection from {addr}")
    message = "Thank you for connecting"
    # because the send() method returns bytes we must convert out message to string with encode()
    c.send(message.encode())
    c.close()