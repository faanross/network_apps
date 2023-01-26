import ipaddress
import os 
import socket
import struct

class IP:
    def __init__(self,buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl= header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        