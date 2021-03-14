from multiprocessing import Queue, Process
import time
import random

# 生產者生產資料並放到queue中
def producer(name, food, q):
	for i in range(5):
		data = '%s do %s %s' %(name, food,i)

		time.sleep(random.randint(1,3))
		print(data)

		q.put(food)

# 消費者把queue中的資料消耗掉，當看到None時，代表已經沒資料了，終止程式
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


	# 解決卡住的問題，等待所有生產者生產完資料後，加一個特殊的符號(None)
	p1.join()
	p2.join()


	# 加None，讓消費者知道已經沒有資料了，讓程式結束運行
	q.put(None)

'''
運行結果
A do beef 0
B do pork 0
D eat beef
A do beef 1
B do pork 1
D eat pork
A do beef 2
A do beef 3
B do pork 2
D eat beef
B do pork 3
A do beef 4
B do pork 4
D eat pork
D eat beef
D eat beef
D eat pork
D eat pork
D eat beef
D eat pork
'''