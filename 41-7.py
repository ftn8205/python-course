"""
同一個進程下多個線程數據是共享的
為什麼同一個進程下還會使用隊列?? 

因為隊列是 管道 + 鎖 組成
所以用隊列也是為了保證數據安全
""" 


import queue


#1 隊列q 先進先出
# q = queue.Queue(3)

# q.put(1)
# q.get()
# q.get_nowait()
# q.get(timeout=3)
# q.full()
# q.empty()

#2 Last in first out queue
# q = queue.LifoQueue(3)

# q.put(1)
# q.put(2)
# q.put(3)

# print(q.get())

#3 優先級Queue  可以給放入隊列中的數據設置進出的優先級 (優先級/值) => 優先級越小越高

q = Queue.PriorityQueue(3)

q.put((1,'111'))
q.put((100,'222'))


