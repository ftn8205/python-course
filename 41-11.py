"""
進程: 資源單位
線程: 執行單位
協程: 程式員自己想出來的 => 單線程下實現並發
	我們程序員自己在代碼層面上監測所有IO操作
	一但遇到IO 我們在代碼級別完成切換
	給CPU的感覺是你在這個程序一直在運行 沒有IO
	從而提升程序的運行效率


多道技術
切換 + 保存 狀態
CPU兩種切換時機
1. 遇到IO
2. 程式長時間占用

TCP服務端的IO操作
accept
recv

代碼要如何做到
切換 + 保存 狀態


切換:
切換不一定是提升效率 也有可能降低效率
IO切 提高效率
沒有IO切 降低效率

保存狀態:
保存上一次我執行的狀態 下一次接著上一次的操作繼續往後執行
yield

"""


# #串行
# import time

# def func1():
# 	for i in range(100000000):
# 		i + 1

# def func2():
# 	for i in range(100000000):
# 		i + 1




# start_time = time.time()
# func1()
# func2()
# print(time.time() - start_time)  11.628109216690063



import time

def func1():
	while True:
		100000000 + 1
		yield

def func2():
	g = func1()  #初始化生成器

	for i in range(100000000):
		i + 1
		next(g)


start_time = time.time()

func2()

print(time.time() - start_time) # 12.866694211959839


# 結論: 計算密集型 頻繁切換 會造成時間 上升