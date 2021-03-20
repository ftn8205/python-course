# Day 38-11


from multiprocessing import Process
import time


def task(name, n):
	print('%s is running' %name)

	time.sleep(n)

	print('%s is over' %name)



if __name__ == '__main__':

	# 創建Process的物件
	p1 = Process(target = task, args = ('jason', 1))
	p2 = Process(target = task, args = ('egon', 2)) 
	p3 = Process(target = task, args = ('tank', 3))  

	start_time = time.time()


	# 啟動process，告訴作業系統幫你創建一個process，是Async的，所以下面三個Process同時執行
	# 不一定會照順序
	p1.start()
	p2.start()
	p3.start()

	p1.join() # 主process等待子process運行結束後才繼續往後執行
	p2.join()
	p3.join()


	print('Main ',time.time() - start_time)


'''
執行結果
jason is running
egon is running
tank is running
jason is over
egon is over
tank is over
Main  3.172908067703247
(時間為3秒多的原因是因為，在join之前這三個Process就同時啟動了，所以是看最久的那個Process要跑幾秒，就大約是那個秒數)

'''