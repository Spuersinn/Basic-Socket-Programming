import socket

# create client socket, using UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get hostname of client, assign port number
udpHost = socket.gethostname()
udpPort = 92500

#get input for message
