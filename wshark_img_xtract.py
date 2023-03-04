from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR = '/home/gitgud/Desktop/pictures/'
PCAPS = '/home/gitgud/Downloads/'
#
Response = collections.namedtuple('Response', ['header', 'payload'])


def get_header(payload):
    try:
        header_raw = payload[:payload.idnex(b'\r\n\r\n')+2]
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None
    

    return header

def extract_content(Response, content_name='image'):
    content, content_type = None, None
    if content_name in Response.header['Content-type']:
        content_type = Response.header['Content-type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]

        if 'Content-Encoding' in Response.header:
            if Response.header['Content-Encoding'] == 'gzip'
        