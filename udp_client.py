import socket

# create client socket, using UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server info
udpHost = socket.gethostname()
udpPort = 62500

# get input for message
clientInput = input("Enter your message:")
clientSocket.sendto(clientInput.encode('utf-8'), (udpHost, udpPort))
