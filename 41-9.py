from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

pool = ThreadPoolExecutor(5)
# 括號內可以傳數字，不傳的話默認會開啟當前計算機CPU個數5倍的線程

"""
池子造出來之後 裡面會固定存在五個線程
這五個線程不會出現重複創建或銷毀的過程
減少創造或銷毀這五個資源的開銷

池子的使用 只需要講需要做的任務往池子中提交即可 自動會有人來服務
"""

def task(n):
	print(n)
	time.sleep(2)
	return n**2

"""

任務提交方式
	同步: 提交任務後 原地等待任務返回的節果 期間不做任何事
	異步: 不等待任務返回結果 直接往下執行
		返回結果如何獲取??
"""

# pool.submit(task, 1) #朝池子中提交任務 異步提交
# print('Main')


t_list = []
for i in range(20): #朝池子中提交20個任務
	res = pool.submit(task, i)

	# print(res.result()) # 會變成同步提交
	t_list.append(res)


#等待線程池中所有任務都執行完後才往下執行 
pool.shutdown() # 關閉現城池 等待線程池中所有任務運行完畢

for t in t_list:
	print('>>>>> ',t.result()) # 是有序的


"""
程序由並發變成串行
res.result() 拿到異步提交的任務的返回結果
"""



