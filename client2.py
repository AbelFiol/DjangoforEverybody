import urllib.request  # Import the module to work with URLs

# Open a URL (http://127.0.0.1:9000/romeo.text) using HTTP GET
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.text')

# Read the response line by line
for line in fhand:
    print(line.decode().strip())  # Decode from bytes to string and remove leading/trailing whitespace