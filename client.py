import socket

# TCP protocol
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 9999))

while True:
	msg = input("input the msg:")
	if len(msg) == 0: 
		continue
	if msg == 'quit':
		phone.send(msg.encode('utf-8'))
		break
	phone.send(msg.encode('utf-8'))
	data = phone.recv(1024)
	print(data.decode('utf-8'))

phone.close()