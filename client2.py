import urllib.request  # Import the urllib.request module for handling URLs.

# Open the URL and create a file-like object to read from the resource.
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

# Loop through each line in the file-like object.
for line in fhand:
    # Decode the line from bytes to a string, strip whitespace, and print it.
    print(line.decode().strip())