GIL 全局解釋器鎖

python解釋器有多個版本，例如Cpython, Jpython....，但普遍使用Cpython，
在Cpython解釋器中，GIL是一把互斥鎖，為了阻止同一個進程下的多個線程同時執行
(同一個進程下的多線程無法利用多核優勢)

=> 因為cpython中的內存管理(垃圾回收機制)不是線程安全的
1. 應用計數
2. 標記清楚
3. 分代回收



重點:
1.GIL不是python的特點而是Cpython解釋器的特點
2.GIL是為了保證解釋器級別的數據安全
3.同一個進程下的多個線程無法同時執行
4.針對不同的數據還是需要家不同的鎖處理
5. 解釋型語言的通病:同一個進程下，多個線程無法利用多核優勢