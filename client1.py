import socket  # Import the socket module for network communication

# Create a TCP socket using IPv4
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server running on the same machine (localhost) at port 9000
mysock.connect(('127.0.0.1', 9000))

# Prepare an HTTP GET request (asking for /romeo.txt)
# NOTE: Technically, you should not use the full URL in a GET request, just the path
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)  # Send the request to the server

# Receive data from the server in chunks of 512 bytes
while True:
    data = mysock.recv(512)  # Receive up to 512 bytes
    if len(data) < 1:  # If no more data is received, break the loop
        break
    print(data.decode(), end='')  # Decode and print the received bytes

# Close the socket connection
mysock.close()