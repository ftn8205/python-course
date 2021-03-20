import socket 
from threading import Thread
from multiprocessing import Process

"""
服務端:
	1. 要有固定的IP和PORT
	2. 24HR 不間斷提供服務
	3. 能夠支持併發
"""

server = socket.socket() # default TCP

server.bind(('127.0.0.1',8080))

server.listen(5)


# 將Thread需要做的功能寫成函數
def talk(conn):
	
	# 通訊循環
	while True:
		try:
			data = conn.recv(1024)

			print(data.decode('utf-8'))
			conn.send(data.upper())

		except:
			print("Error")
			break

	conn.close()


# 鏈結循環
while True:
	conn, addr = server.accept()  # 等待Client端連進來

	# 叫其他人來服務客戶，用Process，Thread都可以
	t = Thread(target=talk, args=(conn,))
	# t = Process(target=talk, args=(conn,))

	t.start()

