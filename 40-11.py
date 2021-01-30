from threading import Thread, Lock
import time

mutex = Lock()
money = 100

def task():
	global money

	#另一種寫法
	with mutex:
		tmp = money
		time.sleep(0.1)
		money = tmp - 1


if __name__ == '__main__':

	t_list = []
	for i in range(100):
		t = Thread(target=task)
		t.start()
		t_list.append(t)



	for t in t_list:
		t.join()

	print(money)

"""
100個線程起來之後，先搶GIL鎖，但遇到網路延遲IO，
所以鎖被釋放掉，導致所有線程還是拿到100，最後結果就是99(100 -1)

如果我們自己加鎖的話:

100個線程起來之後，先搶GIL鎖，
進入IO，GIL自動釋放，但是自己創建的鎖還沒釋放，
其他的線程即使搶到GIL但沒有搶到互斥鎖，
最終GIL還是回到自己手上，並且操作數據
"""