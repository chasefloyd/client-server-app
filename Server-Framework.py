import socket
import select
import sys
from thread import *

# Socket API functions expected to be used
    #Socket() - specifies address family and socket type.
            #AF_INET = internet address for IPv4
            #SOCK_STREAM = socket type for TCP
    #bind() - used to associate the socket with a specific network interface and port number
    #listen() - allows a server to accept() connections.
    #accept() - blocks and waits for incoming connection
            # When a client connects, it returns a new socket object representing the connection
#Select() - allows you to check for I/O completion on more than one socket. So you can call select() to see whcih sockets have I/O ready for reading and/or writing

def serverConnection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Checks to see if correct arguments have been provided to establish Connection
    if len(sys.argv) != 3:
        print("You need to have a script, IP Address, and a port number")
        exit()

    # Takes first argument and assigns to variable 'IP_Address'
    IP_Address = str(sys.argv[1])
    # Takes second argument and assigns to variable 'port'
    Port = int(sys.argv[2])

    # binds server to entered IP address at specified port
    # listens for active connections
    server.listen(50)
    # creates a list of clients connected
    client_list = []

def clientThread(conn,addr):
    #Handles a single client connection
    #sends welcome message to client
    #prints message and address of user who sent message on the server
    #Calls display function to send message to all

def display(message, connection):
    #broadcasts message to clients

def removeConnection(connection):
    #Removes object from list
    #Accepts a connection request and stores socket object and IP address
    #Creates individual thread for each user that connects
