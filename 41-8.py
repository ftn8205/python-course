"""
TCP之前實現併發是來一個人就多開一個進程或線程

開進程跟開線程都需要消耗資源，我們不可能無限的開設進程和線程

池是用來保證計算機安全的情況下，最大限度地利用它
但會降低了程式了運行效率但保證了計算機硬件的安全,讓你的程序能正常運行

"""

import socket
from threading import Thread

def communication(conn):
	while True:
		try: 
			data = conn.recv(1024)
			if len(data) == 0: break
			conn.send(data.upper())

		except ConnectionResetError as e:
			print(e)
			break
	conn.close()


def server(ip,port):
	server = socket.socket()
	server.bind((ip, port))
	server.listen(5)

	while True:
		conn, addr = server.accept()

		#開啟多線程或多進程來處理客戶端通信
		t = Thread(target=communication,args=(conn,))
		t.start()


if __name__ == '__main__':
	s = Thread(target=server,args=('127.0.0.1',8080))
	s.start()




