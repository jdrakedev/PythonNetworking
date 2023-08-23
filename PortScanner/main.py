'''
Port Scanner Using NMAP Module.

This program will take a range of port numbers as input and print wether the state is open or closed.

Ports are thought of as holes in the network.

Routers have firewalls and they protect anything external from getting in.

Lets say you have an online business (e-commerce, blog, etc.), you might have an open port like port 80 for example.
Which will allow people to access your public ip address at port 80, this is bad!

Ideally you dont want any open ports on your network (this is like leaving your door unlocked).

This program will shed the light on any open ports in your network.

To do this we will need the NMAP tool to be installed. We can do so with the command:
pip install python-nmap

'''

import nmap

# start at port 75
begin = 75
# end at port 80
end = 80
# using localhost because doing this on someone else's network is considered illegal
target = '127.0.0.1' 

# instantiate a port scanner object
scanner = nmap.PortScanner()

# loop from the begin port to the end port incremented by one
for i in range(begin, end + 1):
    res = scanner.scan(target, str(i))
    # result will be dictionary containing alot of info, and we only need to check if the port is 
    # open or closed, so we will only access that info in the dictionary
    
    # override the res variable to get back only the items below
    res = res['scan'][target]['tcp'][i]['state']
    
    # print the state of the ports (open/closed) 
    print(f'Port {i} is {res}.')


# GPT

# import nmap

# nm = nmap.PortScanner()
# result = nm.scan('127.0.0.1', '75-80') # 22-443

# for host in nm.all_hosts():
    # print(f"Host: {host}")
    # for proto in nm[host].all_protocols():
        # print(f"Protocol: {proto}")
        # ports = nm[host][proto].keys()
        # for port in ports:
            # state = nm[host][proto][port]['state']
            # print(f"Port: {port}\tState: {state}")

    

