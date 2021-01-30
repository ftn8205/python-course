
import time
# from gevent import monkey
# monkey.patch_all()

from gevent import monkey;monkey.patch_all()
from gevent import spawn

"""
gevent本身無法檢測常見的一些io操作，
在使用的時候必須導入
from gevent import monkey
monkey.patch_all()

還可以簡寫成
from gevent import monkey;monkey.patch_all()
"""


def h():
	print('hh')
	time.sleep(2)
	print('hh')


def ha():
	print('ha')
	time.sleep(3)
	print('ha')


start_time = time.time()

g1 = spawn(h)

g2 = spawn(ha)

g1.join()
g2.join()



print(time.time() - start_time)


"""
原來是五秒，後來變成三秒
"""