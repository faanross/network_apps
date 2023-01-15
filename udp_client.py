# adapted from Black Hat Python for python3

import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto("This is a test.", target_host, target_port)

# receive data
data,addr = client.recv(4096)

print(data)