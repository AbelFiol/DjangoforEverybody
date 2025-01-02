from socket import *  # Importing socket module for network communication.

# Function to create a simple HTTP server.
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)  # Creating a TCP socket (SOCK_STREAM) using IPv4 (AF_INET).
    try:
        # Binding the server to localhost and port 9000.
        serversocket.bind(('localhost', 9000))
        # Listening for incoming connections, allowing up to 5 queued connections.
        serversocket.listen(5)
        
        while True:  # Infinite loop to handle incoming connections.
            # Accepting a connection from a client.
            (clientsocket, address) = serversocket.accept()

            # Receiving data from the client, with a maximum buffer size of 5000 bytes.
            rd = clientsocket.recv(5000).decode()
            # Splitting the received data into lines.
            pieces = rd.split("\n")
            # Printing the first line of the request if it exists.
            if len(pieces) > 0:
                print(pieces[0])

            # Crafting an HTTP response.
            data = "HTTP/1.1 200 OK\r\n"  # HTTP status line indicating success.
            data += "Content-Type: text/html; charset=utf-8\r\n"  # Setting content type as HTML.
            data += "\r\n"  # Blank line to separate headers from the body.
            data += "<html><body>Hello World</body></html>\r\n\r\n"  # HTML response body.
            # Sending the response to the client.
            clientsocket.sendall(data.encode())
            # Shutting down the client socket for writing.
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        # Handling keyboard interrupt (Ctrl+C) to terminate the server gracefully.
        print("\nShutting down...\n")
    except Exception as exc:
        # Handling other exceptions and printing the error message.
        print("Error:\n")
        print(exc)

    # Closing the server socket after exiting the loop or on error.
    serversocket.close()

# Informing the user that the server is accessible and starting it.
print('Access http://localhost:9000')
createServer()