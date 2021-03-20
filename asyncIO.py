import threading
import asyncio


# 在函數前加上async，可以讓此函數變成非同步執行
async def count():
    print("One %s" %threading.current_thread())
    await asyncio.sleep(1)
    print("Two %s" %threading.current_thread())

async def main():

    await asyncio.gather(count(), count(), count())

# 在event loop上監聽 async函數main的執行，當main結束時，event loop也會結束
asyncio.run(main())




'''
運行結果
步驟: 三個count會以非同步的方式執行，所以會幾乎同時列印出三個One，接著三個count同時都去等待一秒鐘的時間，
一秒後，就再繼續執行下一行，幾乎同時列印出三個Two。

One <_MainThread(MainThread, started 4603833792)>
One <_MainThread(MainThread, started 4603833792)>
One <_MainThread(MainThread, started 4603833792)>
(等個一秒)
Two <_MainThread(MainThread, started 4603833792)>
Two <_MainThread(MainThread, started 4603833792)>
Two <_MainThread(MainThread, started 4603833792)>

用async可以讓[單線程實現多併發的效果]
'''