import ipaddress
import os
import socket
import struct
import sys
import threading
import time

SUBNET = '192.168.2.0/24'
MESSAGE = 'WAZAAAAAAAAAA!'

class IP:
    def __init__(self, buff=None):
        header = struct.unpack