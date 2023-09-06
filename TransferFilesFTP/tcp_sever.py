# Server script for a program that uses FTP to transfer files using TCP socket in python

# In this script:
# After setting up a socket were going to accept multiple client connections,
# then we are going to recieve files from the clients, and finally
# were are going to save them on the server.

import socket

if __name__ == "__main__":
    # define the socket parameters
    host = "127.0.0.1" # ip address of the server
    port = 8080 # port number on which the server will listen to the connections
    # next we need the number of clients to connect 
    total_clients = int(input("Enter the number of clients: "))
    # we must now create and bind the socket (create socket object)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this function will specify the address family
    # 1st arg is AF_INET refers to the address family ipv4 (internet protocol version 4) which is the dominant protocol of the net.
    # 2nd arg is SOCK_STREAM refers to a connection oriented TCP protocol.
    
    # bind the socket to the specified port using the bind method
    sock.bind((host, port))
    
    # listen to the client's connections that the user had entered
    sock.listen(total_clients) # takes the maximum number of queued connections as an argument

    # we now want to establish connections with the clients
    connections = []
    print("Initiating clients...")
    
    # server enters a loop to accept multiple client connections, then calls the accept method on the server socket
    # which blocks until a client connection id made. 
    # once a connection is established, the method returns a new socket object and the address of the client
    # the socket object and client address are stored in the connections list for later use
    for i in range(total_clients):
        conn = sock.accept()
        connections.append(conn)
        print(f"Connected with client {i + 1}")
        
    # recieve the files from clients
    fileno = 0
    idx = 0
    # iterate over each client connection stored in the connections list
    for conn in connections:
        idx += 1
        data = conn[0].recv(1024).decode() # takes the connection with the sub-0 (the first connection in the connections list)
        if not data:
            continue
        # create a new file on the server end
        filename = "output"+str(fileno)+".txt" # output 0: File 1, output 1: File 2
        fileno += 1 # file number
        fo = open(filename, 'w')
            while data:
                if not data:
                    break
                else:
                    fo.write(data)
                    data = conn[0].recv(1024).decode()
        # with this we have created a new file on the server with a filename based on the fileno variable
        # the recieved data is written continuously to this file until there is no more data left
        print()
        print("Recieved succesfully!")
        print(f"New filename is {filename}")
        # close the file
        fo.close()
    # close all the connections
    for conn in connections:
        conn[0].close()
