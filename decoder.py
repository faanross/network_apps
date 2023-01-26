import ipaddress
import os 
import socket
import struct

class IP:
    def __init__(self,buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0]
