

import socket
import sys

"""
s = socket.socket()

ip = input("Please enter the IP: ")
port = (input("Please enter the port: "))

s.connect((ip, int(port)))

print(s.recv(1024))         # 1) Ran program at this point. See error on README.md

"""
def banner_grabber(ip, port):
    # Object
    s = socket.socket()
    # Connects to the target
    s.connect((ip, int(port)))
    # Ends program after 30 seconds
    s.settimeout(30)
    print(s.recv(1024))


def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))   
    banner_grabber(ip, port)

main()                      # This works well too.

