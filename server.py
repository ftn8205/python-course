import socket

# 買手機
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 0.0.0.0 => 可以被任何人訪問到
#綁定手機卡
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1', 9999))

#開機
phone.listen(5) # 5 是半連接池的大小

#等待電話請求 (會去半連接池拿東西)
while True:
	(conn, client_addr) = phone.accept()

	print(conn)
	print("client ip and port: ", client_addr)

	# 通信:收發訊息
	while True:
		try:
			data = conn.recv(1024) # 最大接收數據量為 1024Bytes
			if len(data) == 0: 
				break

			print("Client data: ", data.decode('utf-8'))
			
			conn.send(data.upper())
		except Exception:
			break



	#關閉電話連接
	conn.close()

#關機
# phone.close()



