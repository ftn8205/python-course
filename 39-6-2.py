from multiprocessing import Process, Lock
import time, random,json


# look up ticket
def search(i):
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print('user %s look up ticket %s ' %(i, dic.get('ticket_num')))

# buy ticket
def buy(i):

    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)

    time.sleep(random.randint(1,3))

    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1

        with open('data', 'w', encoding='utf-8') as f:
            json.dump(dic,f)
        print('user %s buy ticket success' %(i))

    else:
        print('user %s buy ticket fail' %(i))


def run(i, mutex):
    search(i)

    # 買票環節要加鎖處理
    #搶鎖
    mutex.acquire()
    buy(i)
    # 釋放鎖
    mutex.release()


if __name__ == '__main__':

    # 產生一把鎖，讓所有的子行程去搶，誰先搶到就誰先買到
    mutex = Lock()

    for i in range(1,10):
        p = Process(target=run, args=(i,mutex))
        p.start()
    
