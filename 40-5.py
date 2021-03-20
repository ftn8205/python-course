from threading import Thread
import time

def task(name):
	print("%s is running" %name)
	time.sleep(3)
	print('%s is over' %name)


if __name__ == '__main__':
	t = Thread(target=task, args=('ian',))
	t.start()
	t.join()
	print('Main')