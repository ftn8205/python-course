from threading import Thread
import time

def task(name):
	print("%s is running" %name)
	time.sleep(1)
	print("% is over" %name)




if __name__ == '__main__':

	t = Thread(target=task, args=('ian',))
	t.daemon = True
	t.start()
	print("Main")

