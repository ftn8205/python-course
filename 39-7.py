from multiprocessing import Queue

# 創建一個Queue，是先進先出的。

q = Queue(5) # 可填數字，代表Queue中最大可存放的資料量 

# 放資料到queue中
q.put(111)
q.put(222)
q.put(333)
q.put(444)
q.put(555)
# q.put(666)  # 當資料放滿時，如果還有數資料要放，程序會阻塞，直到有位置讓出來


v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()

# v6 = q.get()  # Queue已經沒有資料時，也會阻塞
# v6 = q.get_nowait()  # 沒資料時，直接報錯
# v6 = q.get(timeout=3) # 沒有資料後等三秒，直接報錯

print(v1, v2, v3, v4, v5)  # 先進先出  111 222 333 444 555
