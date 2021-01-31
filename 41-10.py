from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os


pool = ProcessPoolExecutor(4)
# 括號內可以傳數字，不傳的話默認會開啟當前計算機CPU個數的進程

"""
池子造出來之後 裡面會固定存在幾個進程
這五個進程不會出現重複創建或銷毀的過程
減少創造或銷毀這幾個資源的開銷

池子的使用 只需要講需要做的任務往池子中提交即可 自動會有人來服務
"""

def task(n):
	print(n, os.getpid())
	time.sleep(2)
	return n**2


def callback(n):
	print('callback: ',n.result())

"""

任務提交方式
	同步: 提交任務後 原地等待任務返回的節果 期間不做任何事
	異步: 不等待任務返回結果 直接往下執行
		返回結果如何獲取??
		異步提交任務的返回結果 應該通過回調機制來獲取
		回調機制:
			相當於給每個異步任務綁定一個炸彈
			一但任務有結果 就馬上爆炸
"""


if __name__ == '__main__':
	t_list = []
	for i in range(20): #朝池子中提交20個任務
		res = pool.submit(task, i).add_done_callback(callback)
		t_list.append(res)

