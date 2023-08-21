# This program will help find available wifi networks
# wifi = wireless-fidelity

# This module allows you to spawn processes, connect to their i/o/error pipes, and obtain their return codes
import subprocess 

# create a network object
nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network']) 
# check_output returns info about all the networks available. Args: ['network shell', 'wireless local area network', 'show', 'network']
# netsh is a command line scripting utility that allows one to display or modify the network configuration

# if we run line 8 we get all available networks but they will be displayed in machine code (1's and 0's), so we must decode
decoded_nw = nw.decode('ascii') # decode to ascii (american standard code for information interchange)
print(decoded_nw)


# We can achieve the same thing by running some commands in cmd

# netsh wlan ? (this will give us a list of the commands available)

# netsh wlan show (this will give us a list of all the show commands)

# netsh wlan show all (this will give us a complete wireless system information summary)





