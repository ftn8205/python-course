from multiprocessing import Pool
import os,time


def work(n):
    print('%s run' %os.getpid())
    time.sleep(3)
    return n**2

if __name__ == '__main__':

	#行程池從無到有創建三個行程，接下來都會一直是這三個行程在執行任務
    p=Pool(3)

    res_l=[]

    for i in range(10):
        res=p.apply(work,args=(i,)) # apply 是同步調用，直到本次任务執行完後拿到res。
        res_l.append(res)
    print(res_l)

'''
運行結果

13803 run
13804 run
13805 run
13803 run
13804 run
13805 run
13803 run
13804 run
13805 run
13803 run
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

可看出PID都是固定這三個值，沒有變過。
而且因為是同步調用，所以都會照順序一個一個執行
'''