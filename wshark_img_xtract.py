from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR = '/home/gitgud/Desktop/pictures/'
PCAPS = '/home/gitgud/Downloads/'

Response = collections.namedtuple('Response', ['header', 'payload'])

