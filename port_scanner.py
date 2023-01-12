from queue import Queue
import socket
import threading
import sys

if len(sys.argv) != 3:
    print("Please provide valid CLA: python3 port_scanner.py <threads: 1-100> <mode: 1-3>")
    sys.exit()

threads = int(sys.argv[1])
mode = int(sys.argv[2])

if not (1 <= threads <= 100) or not (1 <= mode <= 3):
    print("Please provide valid CLA: python3 port_scanner.py <threads: 1-100> <mode: 1-3>")
    sys.exit()

target = '192.168.0.102'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# different scanning modes
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

run_scanner(threads, mode)