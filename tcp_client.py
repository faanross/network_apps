import socket

target_host = "google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client to target
client.connect((target_host, target_port))

# send some data once connected
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

# response-handling
response = client.recv(4096)
print(response)