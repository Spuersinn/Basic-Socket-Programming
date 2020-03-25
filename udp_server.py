import socket

# create server socket, using UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get hostname of server, assign port number
udpHost = socket.gethostname()
udpPort = 92500

# bind socket --> use hostname and port we specified earlier
serverSocket.bind((udpHost, udpPort))

# wait for communication from client, print message content along with IP of client
while True:
    print("Server Socket Created. Waiting for Client Connection...")
    message, address = serverSocket.recvfrom(1024)
    print("Received Messages: ", message, "from", address)


