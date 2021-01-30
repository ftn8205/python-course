from multiprocessing import Queue

# 創建一個Queue

q = Queue(5) # 可填數字，代表Queue中最大可存放的數據量 

# 存數據到queue中
q.put(111)
q.put(222)
q.put(333)
q.put(444)
q.put(555)
# q.put(666)  # 當數據放滿時，如果還有數據要放，程序會阻塞，直到有位置讓出來


v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()

# v6 = q.get_nowait()  # 沒數據時，直接報錯
# v6 = q.get(timeout=3) # 沒有數據後等三秒，直接報錯

# v6 = q.get()  # Queue已經沒有數據時，也會阻塞
# print(v1, v2, v3, v4, v5, v6)


"""
q.full()
q.empty()
q.get_nowait()
在多進程的情況下是不精確的，因為你可能剛判斷完，另一個進程就做其他操作了
"""
