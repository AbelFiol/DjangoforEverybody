import socket  # Importing the socket module for network communication.

# Creating a socket for a TCP connection (SOCK_STREAM) using IPv4 (AF_INET).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to the server at 'data.pr4e.org' on port 80 (HTTP).
mysock.connect(('data.pr4e.org', 80))

# Preparing the HTTP GET request command to fetch 'page1.htm'.
# The request uses HTTP/1.0 protocol and ends with double CRLF to signal the end of headers.
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# Sending the encoded HTTP GET request to the server.
mysock.send(cmd)

# Infinite loop to receive the server's response in chunks.
while True:
    # Receiving up to 512 bytes of data at a time from the server.
    data = mysock.recv(512)
    # Breaking the loop if no more data is received (length of data is less than 1).
    if len(data) < 1:
        break
    # Decoding the received data and printing it without adding extra newlines.
    print(data.decode(), end='')

# Closing the socket connection after the response is fully received.
mysock.close()