from multiprocessing import Process, current_process
import time
import os


def task():
	# 拿到現在的PID
	print('%s is running' % current_process().pid)
	print('%s is running' % os.getpid())

	# 拿到父Process的PID
	print('parent of child is %s' % os.getppid())

	time.sleep(3)


if __name__ == '__main__':
	p = Process(target = task)
	p.start()

	p.terminate() # 告訴作業系統殺死當前process，但需要一些時間
	time.sleep(0.1)
	print(p.is_alive()) #判斷當前process是否存活
	print('Main', current_process().pid)
	print('Parent of Main', os.getppid())