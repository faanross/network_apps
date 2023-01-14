import socket

target_host = "192.168.0.102"
target_port = 22

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client to target
client.connect((target_host, target_port))

# send some data once connected
client.send(b"GET / HTTP/1.1\r\nHOST: 192.168.0.102\r\n\r\n")