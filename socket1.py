import socket  # Import the socket library for network communication

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at data.pr4e.org on port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Prepare an HTTP GET request for the web page and encode it into bytes
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Send the HTTP GET request to the server
mysock.send(cmd)

# Continuously receive data in chunks of 512 bytes
while True:
    data = mysock.recv(512)  # Read up to 512 bytes from the socket
    if len(data) < 1:        # If no data is received, end the loop
        break
    print(data.decode(), end='')  # Decode bytes to string and print without adding extra newlines

# Close the socket connection
mysock.close()