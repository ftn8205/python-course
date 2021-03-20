
import time

"""
gevent本身無法檢測常見的一些io操作，
在使用的時候必須導入

from gevent import monkey
monkey.patch_all()

可以簡寫成
from gevent import monkey;monkey.patch_all()
"""

from gevent import monkey;monkey.patch_all()
from gevent import spawn


def h():
	print('1')
	time.sleep(2)
	print('1')


def ha():
	print('2')
	time.sleep(3)
	print('2')


start_time = time.time()
# spawn 可以監管函數中的IO操作，遇到IO時他會切到另一個function，
# 所以當執行中間的sleep時，會在兩個函數不斷來回切換，
# 作業系統這時就會以為沒有IO的產生，就不會把CPU的執行權限拿走 (騙過作業系統)
g1 = spawn(h) 
g2 = spawn(ha)

g1.join() # 在spawn中是非同步執行的，所以要用join等它做完
g2.join()


print(time.time() - start_time)


"""
運行結果
1
2
(等個兩秒)
1
(等個一秒)
2
3.005520820617676  (運行時間只有三秒，達到兩個function並發的效果)
"""