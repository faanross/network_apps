import ipaddress
import os 
import socket
import struct

class IP:
    def __init__(self,buff=None):
        header = struct.unpack('<BBHHH')
