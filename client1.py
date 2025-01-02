import socket  # Import the socket module for network communication.

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server running on localhost (127.0.0.1) at port 9000.
mysock.connect(('127.0.0.1', 9000))

# Prepare the HTTP GET request to fetch the resource 'romeo.txt'.
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Send the encoded HTTP request to the server.
mysock.send(cmd)

# Loop to receive and print the server's response in chunks of 512 bytes.
while True:
    data = mysock.recv(512)  # Receive data from the server.
    if len(data) < 1:  # Exit the loop if no more data is received.
        break
    print(data.decode(), end='')  # Decode and print the received data.

# Close the socket connection to free up resources.
mysock.close()