"""
同一個進程下的多線程無法利用多核優勢，是不是就沒有用了?

單核:四個任務(IO密集型/計算密集型)
多核:四個任務(IO密集型/計算密集型)

# 計算密集型  每個任務需要10秒

單核(不太需要考慮)
	多進程: 額外消耗資源
	多線程: 減少開銷  (X)

多核:
	多進程: 耗時 10秒左右 (X)
	多線程: 耗時 40秒左右 (因為同一個進程下多核無法利用多線程優勢)

# IO密集型 (因為CPU幾乎都在閒置，所以多個CPU也沒有用，用多進程反而浪費更多資源)

多核:
	多進程: 相對浪費資源
	多線程: 更加節省資源

"""

#計算密集型
"""
from multiprocessing import Process
from threading import Thread
import os,time

def work():
	res = 1
	for i in range(1, 50000):
		res *= i


if __name__ == '__main__':
	l = []
	print(os.cpu_count()) # 獲取當前CPU核數
	start_time = time.time()

	for i in range(12):
		# p = Process(target=work)  # 2.5秒
		# p.start()
		# l.append(p)

		t = Thread(target=work)  # 8.29秒
		t.start()
		l.append(t) 

	for t in l:
		t.join()

	# for p in l:
	# 	p.join()

	print(time.time() - start_time)

"""

#IO密集型

from multiprocessing import Process
from threading import Thread
import os,time

def work():
	time.sleep(2)

if __name__ == '__main__':
	l = []
	print(os.cpu_count()) # 獲取當前CPU核數
	start_time = time.time()

	for i in range(400):
		# p = Process(target=work)  # 13.14秒 (產生進程的時間較長)
		# p.start()
		# l.append(p)

		t = Thread(target=work)  # 2秒
		t.start()
		l.append(t) 

	for t in l:
		t.join()

	# for p in l:
	# 	p.join()

	print(time.time() - start_time)

"""
多進程 多線程都有各自的優勢
後面通常都是在多進程下面再開設多線程

既可以利用多核也可以減少資源消耗

"""