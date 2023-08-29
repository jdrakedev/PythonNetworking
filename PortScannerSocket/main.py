'''
This will demonstrate how to make a port scanner using socket (without using NMAP)
'''

# network or port scanning is used as a surveillance tool to identify any open ports available on a particular host.

# tcp ip protocol suit - made of two protocols:
# TCP: from 0 to 65535 ports
# UDP: from 0 to 65535 ports

# its always recommended to close all unused ports on ones network.

# these 65535 ports can be divided into:
# 1. system ports: 0 t0 1023
# 2. registeres ports: 1024 to 49151
# 3. private ports: 49151 and above


# Import necessary modules
from socket import *
import time

# Get the current time for measuring execution time
start_time = time.time()

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Get the target host (IP address) to scan - 127.0.0.1
    target = input('Enter host for scanning: ')
    
    # Get the IP address associated with the target hostname
    t_IP = gethostbyname(target)
    
    # Print the target IP address
    print(f'Starting scanning on host: {t_IP}')
    
    # Loop through a range of port numbers from 50 to 499
    for i in range(50, 500):
        # Create a socket object using IPv4 and TCP protocol
        s = socket(AF_INET, SOCK_STREAM)
        
        # Attempt to establish a connection with the target IP and port
        conn = s.connect_ex((t_IP, i))
        
        # Check if the connection was successful (port is open)
        if conn == 0:
            print(f'Port {i}: OPEN')
        
        # Close the socket connection
        s.close()

# Calculate and print the total time taken for the scanning process
print(f'Time taken: {time.time() - start_time} seconds')


# from socket import *
# import time

# start_time = time.time()

# if __name__ == "__main__":
    # # to avoid illegal activity we will scan on the localhost 127.0.0.1
    # target = input('Enter host for scanning: ')
    # t_IP = gethostbyname()
    # print(f'Starting scanning on host: {t_IP}')
    
    # for i in range(50, 500):
        # s = socket(AF_INET, SOCK_STREAM)
        # conn = s.connect_ex((t_IP, i))
        # if (conn == 0):
            # print(f'Port {i}: OPEN')
        # s.close()
# print(f'Time taken: {time.time() - start_time} ')