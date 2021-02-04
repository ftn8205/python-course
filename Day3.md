### Day3

人 =======> 程式語言 ======> 電腦

程式語言分類:

- 機器語言: 二進制指令 (開發效率低, 執行效率高, 跨平台效率低)
- 組合語言: 把二進制指令用英文代替 (開發效率低, 執行效率高, 跨平台效率低)
- 高級語言
  根據翻譯方式的不同分為:
  - 編譯型語言: 透過編譯器完整翻譯為機器語言，編譯完後，要執行時只要拿編譯過後的機器語言來執行即可，例如C
  - 直譯型語言: 需要一個直譯器，一邊翻譯一邊執行，每次執行都要重新翻譯一次，例如Python 



用Python寫出來的程式，需要由直譯器來解釋，最有名的是用C語言寫出來的CPython直譯器



### Day 4

什麼是變數?

變數為可以變化的數，用來記錄各種事物的狀態，而且事物的狀態是會變化的。

如何使用變數?

先定義變數然後引用它

```python
age = 18    # 定義變量 => 在記憶體中開啟一個位置把18存進去，並且用age去指向它
print(age)  # 引用變量 => 透過age這個變數去記憶體中找到18這個值，並且印出來
```

(畫圖)

變量名的命名原則

最好看到名字就知道他代表什麼意思

只能是字母,數字,下劃線

第一個字不能是數字

不能用到python的關鍵字

風格

在python中 變數名盡量使用 純小寫 + 下劃線

```python
# 例如年齡，第二種寫法就比第一種好
x = 18   (x)
age = 18 (o)

alex_of_age = 30
```

變量值

id: 可以反映變數值的記憶體位址，記憶體位置不同 id就不同

print(id(name)) 查看id號

type:變數型態

age = 18

type(name) 查看type

name = 'Ian'

value: 值本身

print(value)

### is 和 == 的差別

is: 比較左右兩邊的id是否相等

==: 比較左右兩個值是否相等

```python
x = 'ABC'
y = 'EDF'
z = x
print(x is y)   # False
print(x==y)     # True
print(z is x)   # True
print(z==x)     # True
```

**** 但是假如是 m = 10, n = 10,  m is n 會等於True, 主要是因為python直譯器啟動時,會先在記憶體中事先申請好一系列的空間來存放常用的整數(-5, 256)

**常數**: 不會變的量，在python中語法中沒有常數的概念，但通常約定俗成的，會用全部大寫來代表常數

例如 PI = 3.14

**基本數據類型:**

```python
# 1. 數字類型: int, float
age = 18
type(age) # <class 'int'>
money = 10.5
type(money) => # <class 'float'>

# 2. 字串類型: str
name = 'Ian'    #
type(name) # <class 'str'>
long_text = '''用前後三個引號，來放很長的一個字串，還可以換行，
我換行了~~
'''
type(long_text)  # <class 'str'>

# 字串可以跟字串相加，會把兩個字串拼起來，但效率很低，不推薦使用
print('my name is ' + 'Ian')   # my name is Ian
print('=' * 10)  # ==========

# 3. 串列類型: 用索引對應值 索引從0開始
   -5    -4    -3         -2         -1
    0     1    2          3           4
l = [10, 3.1, 'aaa', ['bbb','ccc'], 'ddd' ]
print(l)
print(l[1])
print(l[3])
print(l[3][1])  
print(l[4])
print(l[-1])

# 4. 字典類型: key-value的儲存類型

d = {'name': 'Ian', 'age': 27} 
print(type(d)) #  <class 'dict'>
print(d['name']) # Ian

# 串列 + 字典
students_info = [
    {'name': 'Ian', 'age': 27, 'gender': 'male'},  # 0
    {'name': 'Tom', 'age': 29, 'gender': 'male'},  # 1
]


print(students_info[1]['gender'])  # 取出陣列中的第二個值裡面的gender欄位 => male

# 5. 布林類型: bool，有True和False兩種

is_ok = True
is_ok = False
type(is_ok)  # <class 'bool'>
                                     
```



### 垃圾回收機制

1. 引用計數: 當變數值被綁定的變數名稱的個數為0時，該變數就無法被訪問到，那個變數值所在的記憶體就被回收。

   ```python
   x = 10 
   y = x
   z = x
   # 此時 10 身上的計數為 3
   del x   # 解除 x 與 10 的綁定關係，此時10身上的計數為 2
   z = 12345 # 此時10身上的計數為 1
   del y # 此時10身上的計數為 0，釋放 10 這塊的記憶體空間
   ```

2. 標記清除: 每一段時間掃描記憶體中的stack區，把沒有**直接引用**的值都清掉

3. 分代回收: 存活越久的變數，可能代表它越不容易成為垃圾，



列表在內存空間的儲存方式

l = ['a', 'b']

產生一塊記憶體空間 存 a的記憶體位址 和 b的記憶體位址，並且分別指向存著實際a, b值的地方

(畫圖)

```python

x = 10
l = ['a','b', x]

x  = 123

print(l[2]) # 10
# 因為列表中的x是指向10那個位置的指針，把原來的x指向123並不會影響列表中的那個值

```

