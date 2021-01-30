from threading import Thread, active_count, current_thread
import os, time

def task():
	# print('hello world', os.getpid())
	print('hello world', current_thread().name)
	time.sleep(1)



if __name__ == '__main__':
	t = Thread(target=task)
	t1 = Thread(target=task)
	t.start()
	t1.start()
	# print('Main:', os.getpid())
	# print('Main', current_thread().name)  #線程的名字

	print('Main', active_count()) # 統計當前正在活躍的線程數