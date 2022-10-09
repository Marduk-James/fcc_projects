#   Scans ports to determine which ones are open

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

"""
host = "137.74.187.100"
port = 443

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is open.")
    else:
        print("The port is closed!")

portScanner(port)
"""


host = input("Please enter the IP address you would like to scan: ")
port = int(input("Please enter the port you would like to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is open.")
    else:
        print("The port is closed!")

portScanner(port)