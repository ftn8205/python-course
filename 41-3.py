# 搶鎖時必須要釋放鎖,在操作鎖時很容易遭成死鎖(程市卡死 阻塞)

from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()

#false
# 類只要加括號多次，產生的就是不同的對象
# 如果想要實現加多次括號得到相同的對象 用 單例模式 (Singeton???)

print(mutexA is mutexB) 


class MyThread(Thread):
	def run(self):
		self.func1()
		self.func2()


	def func1(self):
		mutexA.acquire()
		print('%s 搶到A鎖' %self.name) #獲取當前Thread名稱

		mutexB.acquire()
		print('%s 搶到B鎖' %self.name) #獲取當前Thread名稱

		mutexB.release()
		mutexA.release()


	def func2(self):
		mutexB.acquire()
		print('%s 搶到B鎖' %self.name) #獲取當前Thread名稱
		time.sleep(2)

		mutexA.acquire()
		print('%s 搶到A鎖' %self.name) #獲取當前Thread名稱


		mutexA.release()
		mutexB.release()

if __name__ == '__main__':
	for i in range(10):
		t = MyThread()
		t.start()


"""
output: 
Thread-1 搶到A鎖
Thread-1 搶到B鎖
Thread-1 搶到B鎖
Thread-2 搶到A鎖
"""






