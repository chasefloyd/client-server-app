import socket
#serverName = 'servername' #Server IP address
#serverPort = 12000 #Server port number

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9999

clientSocket.connect((host, port))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence)
clientSocket.close()
