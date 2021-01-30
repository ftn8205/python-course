from threading import Thread
import time

def task(name):
	print("%s is running" %name)
	time.sleep(1)
	print("% is over" %name)




if __name__ == '__main__':

	t = Thread(target=task, args=('egon',))
	t.daemon = True
	t.start()
	print("Main")




"""
主線程運行結束後，不會立刻結束，會等待其他非守護線程都結束才會結束
	因為主線程結束的話，所在的進程就會結束，子進程就拿不到進程的資源了
"""