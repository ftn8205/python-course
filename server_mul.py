import socket
import select

server = socket.socket()
server.bind(('127.0.0.1', 8080))

server.listen(5)
server.setblocking(False)

read_list = [server]

while True:

	r_list, w_list, x_list = select.select(read_list, [], [])


	for i in r_list:

		if i is server:
			conn, addr = i.accept()  # 不會阻塞，因為有人連上了才會進到這邊來

			# conn也該被添加到監管的隊列中
			read_list.append(conn)

		else:
			res = i.recv(1024)

			if len(res) == 0:
				i.close()
				read_list.remove(i) # 刪除要監管的對象
				continue

			i.send(b'HiHiHi')

		
