# Socket API functions expected to be used
    #sendall() - sends data from bytes until either all data has been sent or an error occurs
    #recv()
    #close()
    #connect_ex() - used instead of connect() becasue connect() would immediately rise a blockingIOError

def start_connections():
    #Starts by initiating connections
    #types.SimpleNamespace - used to create data we want stored with the socket
    #list(messages) - copied messages the client sends to the server

def service_connection():
    #Keeps track of the number of bytes it's received from the server so it can close its side of the connection

def recieve():
    #Handles receiving messages


def send():
    #Handles sending messages


def close_connection():
    #Close socket connection
    
