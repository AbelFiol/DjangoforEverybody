from socket import *  # Import all socket functions and constants

# Function to create and run the web server
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket using IPv4

    try:
        serversocket.bind(('localhost', 9000))    # Bind the socket to localhost on port 9000
        serversocket.listen(5)                    # Allow up to 5 queued connections

        while(1):  # Infinite loop to keep server running
            (clientsocket, address) = serversocket.accept()  # Accept incoming connection

            rd = clientsocket.recv(5000).decode()  # Receive up to 5000 bytes from client
            pieces = rd.split("\n")                # Split the request by lines

            if (len(pieces) > 0):                  # Print the first line of the request (e.g., GET / HTTP/1.1)
                print(pieces[0])

            # Prepare a simple HTTP response with an HTML body
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"  # Blank line to indicate end of headers
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())         # Send the full HTTP response
            clientsocket.shutdown(SHUT_WR)              # Close writing side of the client socket

    except KeyboardInterrupt:
        print("\nShutting down...\n")  # Gracefully shut down on Ctrl+C
    except Exception as exc:
        print("Error:\n")
        print(exc)  # Print any other errors
    
    serversocket.close()  # Close the main server socket when done

print('Access http://localhost:9000')  # Show URL to test the server
createServer()  # Start the server