from multiprocessing import Queue, Process
import time
import random

def producer(name, food, q):
	for i in range(5):
		data = '%s do %s %s' %(name, food,i)

		time.sleep(random.randint(1,3))
		print(data)

		q.put(food)


def consumer(name, q):
	while True:
		food = q.get()

		if food is None:
			break

		time.sleep(random.randint(1,3))
		print('%s eat %s' %(name, food))



if __name__ == '__main__':

	q = Queue()

	p1 = Process(target=producer,args=('A','beef',q))
	p2 = Process(target=producer,args=('B','pork',q))

	c1 = Process(target=consumer,args=('D',q))

	p1.start()
	p2.start()
	c1.start()


	#解決卡住的問題，等待所有生產者生產完數據後，加一個特殊的符號
	p1.join()
	p2.join()


	# 加None，一定在queue的最後一個
	q.put(None)