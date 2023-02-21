from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    if packet[TCP].payload
    