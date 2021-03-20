import socket
import time 
from gevent import monkey;monkey.patch_all()
from gevent import spawn

def communication(conn):
	while True:
		try:
			data = conn.recv(1024)
			if len(data) == 0:
				break
			conn.send(data.upper())
		except ConnectionResetError as e:
			print(e)
			break

	conn.close()
	

def server(ip, port):
	server = socket.socket()

	server.bind((ip, port))
	server.listen(5)

	while True:
		(conn, addr) = server.accept()
		spawn(communication, conn) # 監測communication的IO (recv)



if __name__ == '__main__':
	g1 = spawn(server, '127.0.0.1', 8080) # 監測server的IO (accept)
	g1.join()