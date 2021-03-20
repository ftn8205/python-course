import socket
import time 

server = socket.socket()

server.bind(('127.0.0.1', 8080))
server.listen(5)

# 預設是True (阻塞)
# 如果改成False => 將所有網路阻塞變成非阻塞
server.setblocking(False)


r_list = []
del_list = []

while True:
	try:
		conn, addr = server.accept()
		r_list.append(conn)

	except BlockingIOError:

		for conn in r_list:
			try:

				data = conn.recv(1024) 

				if len(data) == 0: # client 斷開連接
					conn.close() # 關閉conn

					# 將無用的conn 從 r_list刪除

					del_list.append(conn)
					continue

				conn.send(data.upper())



			except BlockingIOError: # 因為是非阻塞，recv如果沒收到資料，它不會去等而是噴這個exception
				continue

			except ConnectionResetError: # 當客戶端斷開連結，recv會噴這個error
				conn.close()
				del_list.append(conn)

		# 把斷開的conn 刪掉
		for conn in del_list:
			r_list.remove(conn)

		del_list.clear()



