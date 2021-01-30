from multiprocessing import Queue, Process


def producer(q):
	q.put('I am Ian')


def consumer(q):
	print(q.get())



if __name__ == '__main__':

	q = Queue()

	p = Process(target=producer,args=(q,))
	p1 = Process(target=consumer,args=(q,))
	p.start()
	p1.start()

	# print(q.get())