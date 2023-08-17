# Chat Room Connection - Client To Client

import threading 
import socket

# Thread: a sequence of instructions within a program (running many threads is like running many programs)
# TODO: set a host ip and a port for the server to run on 

# this will be our local host 
host = "127.0.0.1"

# here we need to be careful not to choose a reserved board
# to be sure when can run "netstat" in cmd, and avoid those open ports
port = 59000

# next we create a server object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now we bind the server to the host 
server.bind((host, port)) 

# active the listening mode for any incoming connections to the server
server.listen()

# create a list for clients
clients = []

# create a list for aliases
aliases = []

# create a function that sends a message from the server to all the connected clients
def broadcast(message):
    # iterate through the list of clients, and for each client send a message
    for i in clients:
        i.send(message)

# next we need a function that will handle the connections of each client computer so when clientA connects to the server
# and sends a message to clientB we want to recieve the message from clientA and send it to clientB
def handle_client(client):
    while True:
        try:
            message = client.recv(1024) # max ammout of bytes the server can recieve from a single client
            broadcast(message)
        except:
            #if error: we must identify the client that need to get rid of from the clients list 
            idx = clients.index(client)
            # then we remove that client 
            clients.remove(client)
            # then close the connection with that client
            client.close()
            # we will do the same with the aliases
            alias = aliases[index] # here we have overwritten the value of the alias
            broadcast(f"{alias} has left the chat!".encode("utf-8")) # needs to be sent in bytes so we use encode()
            aliases.remove(alias)
            # after removing client and alias break
            break

# now we need a main function to recieve the clients connection
def recieve():
    while True:
        print("The server is running and listening...")
        # prep the server to accept any incoming connections
        client, address = server.accept()
        print(f"Connection is establish with {str(address)}") # address is an int
        # next we send a word to the client (to inform it of what the alias is)
        client.send("alias?".encode("utf-8"))
        # create that alias based on the inforamtion recieved from the client
        alias = client.recv(1024)
        # append this alias to the list of aliases 
        aliases.append(alias)
        # append this client to the list of clients
        clients.append(client)
        # display a message in the server saying what the alias of this client is, and will return the alias of this user
        print(f"The alias of this client is {alias}".encode("utf-8"))
        # send a message to all the connected users, telling them that this user has joined the chatroom
        broadcast(f"{alias} has connected to the chat!".encode("utf-8"))
        # send a message from the server to this client telling them that they are connected
        client.send("You are now connected!".encode("utf-8"))
        # we must now create and start the thread 
        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    recieve()




 
