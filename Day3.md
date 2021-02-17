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

---

shallow and deep copy

```python
list1 = ['Ian', 'Tom', [1,2]]
list2 = list1
# 兩者分隔不開, 一個改了另一個就會跟著改
# 若要分開的話, 可以用copy, 產生一個新的列表

# shallow copy (把原列表第一層的記憶體位址，copy給新列表，對不可變類型可以分開量惡個列表,若有可變類型的話就沒辦法區分)
list3 = list1.copy()
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list3[0]), id(list3[1]), id(list1[2]))

# deep copy (若要完全分開，用deep copy)
import copy
list3 = copy.deepcopy(list1)
				    不可變      不可變         可變
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list3[0]), id(list3[1]), id(list3[2]))
# 140296820201072 140296820201456 140296820033280
# 140296820201072 140296820201456 140296820260672

print(id(list1[2][0]),id(list1[2][1]))
print(id(list3[2][0]),id(list3[2][1]))
# 4418722144 4418722176
# 4418722144 4418722176

```

函數

```python
'''
函數的目的是為了減少重複的程式碼
'''

# 1. 無參數函數
def func():
  print('Hi!')

func()

# 定義函數發生的事情
1. 申請內存空間 保存函數的代碼
2. 講上述內存地址 綁定函數名
3. 只檢查語法，不執行代碼

# 調用函數發生的事情
1. 通過函數名找到函數的內存地址
2. 加()來觸發函數的執行

def foo():
  bar()
  print('from foo')
  
def bar():
  print('from bar')

foo()

'''
from bar
from foo
'''

# 2. 有參數的函數
def func(x,y):
  print(x,y)
  
func(1,2)


# 3. 函數返回值
def func(x,y):
  print('111')
  return x + y
	print('222')

func(1,2)

'''
return是函數結束的標誌，會直接跳出函數，並且返回return 後面的值，什麼都不寫則返回None
'''
```

Day 14

```python
def func(x,y):
  print(x,y)

func(1,2)

'''
在調用階段，會把1,2這兩個變數值綁定給函數的變量名x, y
只在函數裡面有綁定關係
函數結束後就解除綁定關係


1. 位置參數:
必須被傳值，多一個少一個都不行

位置實參:
按照順序與行參一一對應
func(111,222)

2. 關鍵字參數:
關鍵字實參 => 在函數調用階段,按照key=value方式傳入
func(y=4,x=1)

3. 默認參數:
默認行參 => 在定義函數階段，就已經被賦值的參數，在調用階段要不要賦值都可以

def func(x,y=3):
	print(x, y)
	
4. 可變長度的參數
在調用函數時，傳入的實參的個數不確定

a. *: 用來接受溢出的值，會用Tuple存起來，後面名字可以隨便定，但通常會寫*args
def func(x,y,*args):  # args = (3,4,5,6)
	print(x,y,args)
	
func(1,2,3,4,5,6)

b. **: 用來接收溢出的值，會用字典存起來，通常會寫**kwargs

def func(x,y,**kwargs):
	print(x,y,kwargs)
func(1,y=2,a=1,b=2,c=3)

c: * 也可用在實參中，會打散後面的值
def func(x,y,z):
	print(x,y,z)
	
func(*[11,22,33])

d: 形參與實參都帶*
def func(x,y,*args): # args = (3,4,5,6)
	print(x,y,args)

func(1,2,*[3,4,5,6])


** 在實參中
def func(x,y,z):
	print(x,y,z)  # 1 2 3

func(**{'x':1,'y':2,'z':3}) # func(x=1,y=2,z=3)

都帶**

def func(x,y,**kwargs):
	print(x,y,kwargs) # 111 222 {'a':333, 'b':444}

func(**{'y':222,'x':111,'a':333,'b':444})

'''
```

Day 15

Stack : 變量名字跟內存地址的對應關係

全局範圍:

內置名稱空間

全局名稱空間

局部範圍:

局部名稱空間

---

Namespace: 

1. 內置名稱空間: 存放python 解釋器內置的名字(print..)

   存活週期:python解釋器啟動時產生, python解釋器關閉則銷毀

2. 全局名稱空間:不是函數內定義的，也不是內置的，剩下的都是全局名稱
   存活週期:python程序執行則產生，運行完畢後銷毀

3. 局部名稱空間: 在調用函數時，運行函數體代碼時產生的函數內的名字
   存活週期: 調用函數時存活，調用完後銷毀

產生的順序:
內置名稱空間 > 全局 >局部

查找順序:當前位置一層一層向上找

如果現在在局部空間:

局部 -> 全局 -> 內置

如果現在在全局空間:

全局 -> 內置

---

名稱空間的千套關係 以函數定義階段為主，與調用位置無關

```python
x = 1
def func():
  print(x)
def foo():
  x = 222
  func()
foo()  # 1
```

全局作用域: 全局,內置

1.全局存活

2.全局有效

局部作用域: 局部

1.臨時存活

2.局部有效:函數內有效

```python
# 如果在局部想要修改全局的名字對應的值(不可變類型)，需要用global

x = 111

def func():
  global x
  x=222
  
func()
print(x) # 222
```

Day 16

可以把函數當作變數來用，func=內存地址

```python
def func():
  print('from func')

# 1. 可以賦值
f = func
print(f, func)
f()

# 2. 可以當函數的參數傳入
def foo(x):
  print(x)
foo(func) # foo(func的內存地址)

#3. 可以當作另一個函數的返回值
def foo(x):
  return x

res = foo(func)
print(res)

# 4. 當作容器類型的元素
l = [func,]
print(l)
l[0]()

dic = {'k1':func}
print(dic)
dic['k1']()
------

閉包函數
閉: 該函數是內嵌函數
包: 該函數包含對外層函數作用域名字的引用 (不是對全局作用域)
def f1():
  def f2():
    print('f2')
  return f2

f = f1()
print(f) # f2的內存地址

# 必包函數的應用
兩種船參的方式
1. 直接把函數體需要的參數定義成形參

def f2(x):
  print(x)
f2(1)
f2(2)

2. 方式二:
def f1(x):
  def f2():
    print(x)
  return f2

x=f1(3)
print(x)
x()
```

Day 17

```python
# 如果只能傳值給wrapper，但又要將這些值全部傳給裡面的index的話
def wrapper(*args, **kwargs): 
  index(*args, **kwargs) # index(111,222,a=333,b=444)
  
wrapper(111,222,a=333,b=444)


'''
什麼是裝飾器:
器指的是工具，可以定義成函數
裝飾：為其他事物添加額外的東西來點綴

裝飾器: 定義一個函數，該函數用來為其他函數增加額外的功能

why 裝飾器
開放封閉原則:
開放:對拓展功能開放
封閉:對修改源代碼封閉

裝飾器就是在不修改源代碼以及調用方式的前提下，增加新功能


'''
# 裝飾器模板
def outter(func):
  def wrapper(*args,**kwargs):
    # 1. 調用原函數
    # 2. 新增新功能
    res = func(*args, **kwargs)
    return res
  return wrapper

# 用模板改成執行時間的裝飾器
from functools import wraps
def outter(func):
  
  @wraps(func) # 把原函數的屬性賦值給wrapper
  def wrapper(*args,**kwargs):
    # 1. 調用原函數
    # 2. 新增新功能
    start = time.time()
    res = func(*args, **kwargs)
    end = time.time()
    print(end-start)
    return res
  return wrapper

# 在被裝飾對象用＠裝飾器名字 
@outter  # index = outter(index)
def index(x,y):
  print('index %s %s' %(x,y))

index(111,222)


```

Day18

```python
def auth(db_type):
  def deco(func):
    def wrapper(*args,**kwargs):
      name = input('name:')
      pwd = input('pwd:')
			
      if db_type == 'file':
        if name == 'ian' and pwd == '123':
          print('success')
          res = func(*args, **kwargs)
          return res
        else:
          print('login fail')
      else:
        print('not support!')
    return wrapper


@auth(db_type='file') 
# 先跑auth(db_type='file') 會變成 => @deco => index=deco(index) => wrapper
def index(x,y):
	print(x,y)
  
index(1,2)

# 有參裝飾器模板

def deco(x):
  def outter(func):
    def wrapper(*args,**kwargs):
      # 1. 調用原函數
      # 2. 新增新功能
      res = func(*args, **kwargs)
      return res
  	return wrapper
  return outter
```

```python
'''
每次重複的結果都跟上次有關聯
'''
# 調用__iter__方法會將其轉換成迭代器對象
d = {'a':1, 'b':2, 'c':3}
res = d.__iter__()
print(res)
print(res.__next__()) # a
print(res.__next__()) # b
print(res.__next__()) # c
print(res.__next__()) # 已經沒值了，會有exception

# 若想再從頭遍歷一次，要再重新宣告一次才行
res = d.__iter__()

# 1. d.__iter__() 得到一個迭代器對象
# 2. 迭代對象.__next__() 拿到一個返回值，然後將其返回值賦值給k
# 3. 重複步驟二，直到拋出異常，for循環會捕捉異常然後結束迴圈
for k in d:
  print(k)
```

```python
'''
在函數內一但存在yield的關鍵字，調用函數並不會執行函數代碼，會產生一個生成器。
'''
def func():
  print('no.1')
  yield 1
  print('2')
  yield 2
g = func()
print(g)
# 生成器就是一種自定義的迭代器
g.__iter__()

'''
會觸發函數體的運行，遇到yield就停下來，將yield後的值當作本次調用的結果
'''
res = g.__next__()  
print(res)
'''
no.1
1
'''
res2=g.__next__()
print(res2)
'''
no.2
2
'''
res3=g.__next__()
print(res3)
'''
沒值了，會報錯
'''
len('aaa') # 'aaa'.__len__()
next(g) # g.__next__()
iter(可迭代對象) # g.__iter__()

```

Day 19

```python
def dog(name):
  print("start")
  while True:
    x = yield
    print('After yield: %s %s' %(name,x))
    
    
g = dog('alex')
g.send(None) # 等於next(g)  start

g.send('bone') # After yield: alex bone
g.send('cat')  # After yield: alex cat

# 三元表達式
res = 11111 if x > y else 2222

#列表生成式
l = ['a','b','c','d']
new_l = []
# 1
for name in l:
  new_l.append(name)
# 2
new_l = [name for name in l]

# 字典生成式
keys = ['name','age','gender']
dic = {key:None for key in keys}


```

Day 20

```python
# function
def func(x,y):
  return x + y

# analoumou function，用於臨時調用一次的場景
lambda x,y:x+y

# 調用匿名函數

```

