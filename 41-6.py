# 一些進程/線程需要等待另外一些進程/線程 執行完畢後才能運行。

from threading import Thread, Event
import time

event = Event()

def light():
 	print('red light')
 	time.sleep(3)
 	print('green light')
 	event.set()



def car(name):
 	print('%s waiting for red light' %name)
 	event.wait()  # 等待別人發消息給你
 	print('%s gogo' %name)


if __name__ == '__main__':
 	t = Thread(target=light)
 	t.start()


 	for i in range(20):
 		t = Thread(target=car,args=('%s' %i,))
 		t.start()