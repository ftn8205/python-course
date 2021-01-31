# Day 38-10


from multiprocessing import Process
import time


def task(name):
	print('%s is running' %name)

	time.sleep(3)

	print('%s is over' %name)



if __name__ == '__main__':

	# 創建一個對象
	p = Process(target = task, args = ('jason',)) 

	# 開啟process, 告訴作業系統幫你創建一個process  Async

	p.start()

	print('Main')