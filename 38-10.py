# Day 38-10


from multiprocessing import Process
import time


def task(name):
	print('%s is running' %name)

	time.sleep(3)

	print('%s is over' %name)



if __name__ == '__main__':

	# 創建一個Process的物件，指定這個Process要執行的函數，以及該函數所需要的參數
	p = Process(target = task, args = ('jason',)) 

	# 啟動process，告訴作業系統幫你創建一個process，是Async的
	p.start()

	print('Main')


'''
執行結果:
Main
jason is running
jason is over
'''