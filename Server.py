import socket
import select
import sys
from thread import *

# AF_INET = 1. address domain of the socket, 2. socket type
# SOCK_STREAM = data/characters are read in a continuous flow

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Check to see if correct number of arguments has been provided
if len(sys.argv) != 3:
    print("You need to have a script, IP Address, and a port number")
    exit()

# Takes first argument and assigns to variable 'IP_Address'
IP_Address = str(sys.argv[1])
# Takes second argument and assigns to variable 'port'
Port = int(sys.argv[2])


# Binds server to IP address at Port
server.bind((IP_Address, Port))

# server listens for up to 50 active connections
server.listen(50)

# puts clients on server in a list
client_list = []
