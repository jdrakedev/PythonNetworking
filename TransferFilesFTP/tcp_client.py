# We will be using FTP (file transfer protocol) to transfer files using TCP socket in python

# In this script:
# We write the logic for the client that will connect to the server

import socket

if __name__ == "__main__":
    host = "127.0.0.1" 
    port = 8080 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # call the connect method on the client socket object to establish a connection with the server
    # it will take the servers ip address and the port number as aruguments 
    while True:
        filename = input("Filename to be transfered: ")
        try:
            fi = open(filename, 'r')
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).endcode())
                data = fi.read()
            fi.close()
        except IOError:
            print("Invalid filename...")

