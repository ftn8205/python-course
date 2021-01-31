# Day 38-11


from multiprocessing import Process
import time


def task(name, n):
	print('%s is running' %name)

	time.sleep(n)

	print('%s is over' %name)



if __name__ == '__main__':

	# 創建一個對象
	p1 = Process(target = task, args = ('jason', 1))
	p2 = Process(target = task, args = ('egon', 2)) 
	p3 = Process(target = task, args = ('tank', 3))  

	# 開啟process, 告訴作業系統幫你創建一個process, 是Async的
	# 不一定會照順序

	start_time = time.time()

	p1.start()
	p2.start()
	p3.start()

	p1.join() #主process 等待 子process運行結束後才繼續往後執行
	p2.join()
	p3.join()


	print('Main ',time.time() - start_time)