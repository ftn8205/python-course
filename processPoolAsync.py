from multiprocessing import Pool
import os,time

def work(n):
    print('%s run' %os.getpid())
    time.sleep(3)
    return n**2

if __name__ == '__main__':

    # 行程池從無到有創建三個行程，接下來都會一直是這三個行程在執行任務
    p=Pool(3)
    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,)) # 使用apply_async 非同步執行
        print(res) 
        res_l.append(res)

    # 使用非同步的話，主行程需要使用join，等待行程池内任务都處理完畢，然後用get來取得資訊。
    # 如果沒有join的話，主行程结束，行程池可能還來不及執行，就跟著一起结束了。

    p.close()
    p.join()
    
    for res in res_l:
        # 因為是非同步執行的，所以一開始res還拿不到真正的資訊，要等所有行程池都執行完畢，再使用get來獲取apply_async的結果。
        # 如果是apply，则没有get方法，因為apply會等到他做完回傳結果，才執行下一個。
        print(res.get()) 

'''
運行結果
14020 run
14019 run
14021 run
14020 run
14019 run
14021 run
14020 run
14019 run
14021 run
14019 run
0
1
4
9
16
25
36
49
64
81

'''