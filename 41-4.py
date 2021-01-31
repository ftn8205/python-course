# 41-4

# 遞歸鎖: 
# 可以被連續的acquire和release
# 但是只能被第一個搶到這把鎖的來執行上述操作
# 他的內部有一個計數器,每acquire一次就加一,每release一次就減一
# 只要次數不為0 那麼其他人點無法搶到該鎖


# 41-5
# 信號量:
# 如果互斥鎖是廁所的話，信號量就相當於多個廁所



from threading import Thread, Semaphore
import time
import random


sm = Semaphore(5)  #括號數字 寫多少就有幾個空位

def task(name):
	sm.acquire()
	print('%s is using' % name)
	time.sleep(random.randint(1,5))
	sm.release()

if __name__ == '__main__':

	for i in range(20):

		t = Thread(target=task, args=('number: %s' %i, ))
		t.start()