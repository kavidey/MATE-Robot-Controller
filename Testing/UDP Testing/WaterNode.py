import socket
import time

UDP_IP = "169.254.23.12"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	v = input("Message:   ")
	MESSAGE = v.encode()
	sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))