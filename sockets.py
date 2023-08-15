'''
Socket Programming in Python
'''

# socket programming is a way of connection between two nodes (or sockets) to communicate with each other.

# one socket listens to a particular port at an ip, while the other socket reaches out to the other to establish a connection.

# the server forms the listener socket while client reaches out to the server.

#--------------------------------------------------------------------------------------------------------------------------------------------------

# AF_INET refers to the address family ipv4 (internet protocol version 4), which is the dominant protocol of the internet

# SOCK_STREAM refers to the connection oriented TCP (transmission control protocol), and this means a mode where a connection 
# is established before any data is transferred.

# NOTE: if any error occurs during the creation of a socket the a socket.error is thrown, and we can only connect to a server via ip address

import socket 
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket successfully created")
except socket.error as err:
    print(f"socket creation failed with error {err}")

port = 80

try:
    host_ip = socket.gethostbyname("www.github.com")
except socket.gaierror:
    # socket.gaierror means theres a problem with the DNS (domain name service)
    print("error resloving the host")
    sys.exit()
# connect to the server 
s.connect((host_ip, port))
print(f"Socket has successfully connected to Github on port == {port}")

# this will print the ip address of a given website
# ip = socket.gethostbyname('www.github.com')
# print(ip) 