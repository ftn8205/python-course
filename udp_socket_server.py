import socketserver


class MyRequestHandle(socketserver.BaseRequestHandler):
	def handle(self):

		# (b'content', <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('127.0.0.1', 9000)>)
		print(self.request) 

		client_data = self.request[0]
		server = self.request[1]
		client_address = self.client_address

		print(client_data)
		server.sendto(client_data.upper(), client_address)



s = socketserver.ThreadingUDPServer(('127.0.0.1', 9000), MyRequestHandle)


'''
下面這行相當於

循環的去接收Client傳來的訊息
while True:	
    msg,addr=udp_server_client.recvfrom(1024)

接著開一個Thread去處理後續的事情，做的事情就定義在上面那個class的handle方法中

'''
s.serve_forever()
