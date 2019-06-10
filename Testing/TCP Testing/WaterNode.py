import socket

HOST = '169.254.23.12'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

wtr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	wtr.connect((HOST, PORT))
	wtr.sendall('Hello, world'.encode())
	data = wtr.recv(1024)

	print('Received', repr(data))

except:
	wtr.close()