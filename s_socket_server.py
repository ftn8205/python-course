import socketserver

class MyRequestHandle(socketserver.BaseRequestHandler):
	def handle(self):
		print(self.request) # conn
		print(self.client_address) # client_addr

		while True:
			try:
				data = self.request.recv(1024) 
				if len(data) == 0: 
					break

				print("Client data: ", data.decode('utf-8'))
				
				self.request.send(data.upper())
			except Exception:
				break

		self.request.close()



s = socketserver.ThreadingTCPServer(('127.0.0.1', 9001), MyRequestHandle)


'''
下面這行等同於

while True:
	(conn, client_addr) = phone.accept()

也就是循環的從connection pool中取出連線請求，並與其連線

接著開一個Thread，把每一個連接對象交給不同的Thread去服務，而Thread做的事情就是定義在上面那個class的handle方法中
'''
s.serve_forever()


