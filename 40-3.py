from threading import Thread
import time

# 產生線程的方式
# 方法一

def task(name):
	print('%s is running' %name)
	time.sleep(1)
	print('%s is over' %name)



# 開啟線程不需要在main下面執行代碼，但還是習慣在main下面寫

t = Thread(target=task,args=('egon',))

t.start()

print("Main")




#方法二

class MyThread(Thread):
	def __init__(self, name):
		# 如果要重寫別人的方法，但不知道別的方法裡面有啥，就先調用父類的方法
		super().__init__()
		self.name = name


	def run(self):
		print("%s is running" %self.name)
		time.sleep(1)
		print('END')


if __name__ == '__main__':
	t = MyThread('egon')
	t.start()
	print('Main')
