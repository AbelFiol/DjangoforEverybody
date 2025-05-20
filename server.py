from socket import *

# Function to create and run a basic web server
def createServer():
    # Create a TCP/IP socket using IPv4
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Bind the socket to localhost on port 9000
        serversocket.bind(('localhost', 9000))

        # Listen for incoming connections (up to 5 in queue)
        serversocket.listen(5)

        # Infinite loop to handle incoming client requests
        while True:
            # Accept a client connection
            (clientsocket, address) = serversocket.accept()

            # Receive up to 5000 bytes from the client and decode to string
            rd = clientsocket.recv(5000).decode()

            # Split the request by newline to process headers
            pieces = rd.split("\n")

            # Print the first line of the request (usually the HTTP GET line)
            if len(pieces) > 0:
                print(pieces[0])

            # Prepare a basic HTTP response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            # Send the response to the client
            clientsocket.sendall(data.encode())

            # Close the sending side of the connection
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C to shut down the server
        print("\nShutting down...\n")
    except Exception as exc:
        # Handle any other exceptions and print the error
        print("Error:\n")
        print(exc)

    # Close the server socket
    serversocket.close()

# Print server access message
print('Access http://localhost:9000')

# Start the server
createServer()