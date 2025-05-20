import socket  # Import the socket library to enable network communication

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at data.pr4e.org on port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Prepare the HTTP GET request and encode it to bytes
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Send the request to the server
mysock.send(cmd)

# Receive and print the response in chunks of 512 bytes
while True:
    data = mysock.recv(512)  # Receive up to 512 bytes of data
    if len(data) < 1:        # Break the loop if no more data is received
        break
    print(data.decode(), end='')  # Decode and print the data without adding extra newlines

# Close the socket connection
mysock.close()