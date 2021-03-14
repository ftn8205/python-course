from multiprocessing import Process
import time

def task():
	print('sub process is alive')
	time.sleep(3)
	print('sub process is dead')

if __name__ == '__main__':
	p = Process(target = task)

	p.daemon = True  # 將p設為守護行程，必須寫在 p.start() 之前，否則會有exception

	p.start()
	print('Main Process is dead')

'''
輸出結果
Main Process is dead

因為父行程結束後，子行程就會跟著結束，所以執行不到子行程的function
'''