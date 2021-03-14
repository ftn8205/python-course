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
  return deco
  

# 先跑auth(db_type='file') 會變成 => @deco => index=deco(index) => wrapper
@auth(db_type='file') 
def index(x,y):
	print(x,y)
  
index(1,2)

# 有參裝飾器模板

def deco(x):
  def outter(func):
    def wrapper(*args,**kwargs):
      # 1. 在此調用原函數
      # 2. 然後新增新功能
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

```python
'''
模塊: 一系列功能的集合體
1. 內置模塊
2. 第三方模塊
3. 自定義的模塊
 ex: 一個python文件，文件名m.py 模塊名就叫m
'''
import foo
# 1. 執行foo.py
# 2. 產生foo.py 的名稱空間, 將foo.py運行過程中產生的名字都丟到foo的名稱空間中
# 3. 在當前文件中產生一個名字foo，並且指向2中所產生的名稱空間

# 引用: 模塊名.名字
foo.x
foo.get()

# 導入模塊方式
import time, foo, m 
import foo as f
f.x


```

Day21

```python
'''
1. 文件被作為模塊導入
print(__name__) # 文件名
2. 若是文件直接被執行
print(__name__) # __main__
'''

# import 導入模塊的優缺點
# 優點:必須加前綴，部會與當前名稱空間的變數衝突
# 缺點: 加前綴麻煩
import foo
foo.x

# from .. import...
'''
1. 產生一個模塊的名稱空間
2. 運行foo.py，將運行過程中產生的名子丟到模塊的名稱空間中
3. 在當前名稱空間拿到一個名字，該名字指向 模塊空間中的某一個內存地址

優點:不用加前綴
缺點:容易與當前名稱空間混淆
'''
from foo import x
from foo import get

'''
優先級
1. 內存 (內置模塊)
2. 依照sys.path中存放文件的順序依次去找要導入的模塊
'''
import sys
# 值為一個列表，其中第一個文件夾是當前執行文件所在的文件夾
print(sys.path)

#查看在內存中的模塊
print(sys.modules)
```

```python
'''
包是一個有包含有__init__.py文件的文件夾，是模塊的一種形式，包被用來當作模塊導入
mmm
  -- __init__.py
  
1. 產生一個名稱空間
2. 運行包下的__init__.py文件，將運行過程中產生的名字都丟到1的名稱空間中
3. 在當前執行文件的名稱空間中拿到一個名字mmm, mmm指向1的名稱空間
'''
import mmm

'''
在__init__.py 加
絕對導入: 以包的文件夾作為起始來進行導入
from foo.m1 import f1
from foo.m2 import f2
from foo.m3 import f3
'''

```

Day22

```python
import time
# 1. timestamp
# 用於時間間隔的計算
print(time.time())

# 2. 按照格式顯示的時間
# 用於顯示時間
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))

# 3. 結構化時間
# 可以單獨獲取時間的某部分
res = time.localtime()
print(res)
print(res.tm_year)
print(res.tm_yday)

# datetime
import datetime
print(datetime.datetime.now() + datetime.timedelta(days=3))

# 操作
#1. 時間格式的轉換
# struct_time -> timestamp
s_time=time.localtime()
print(time.mktime(s_time))

# timestamp -> struct_time 
time.localtime(time.time())

# GMT+8
time.localtime()
# GMT+0
time.gmtime()


#struct_time -> format time
s_time = time.localtime()
time.strftime('%Y-%m-%d %H:%M:%S', s_time)

# format time  ->struct_time
1988-03-03 11:11:11
time.strfttime('1988-03-03 11:11:11', '%Y-%m-%d %H:%M:%S')

# format string -->  struct_time --> timestamp
# 1988-03-03 11:11:11

struct_time = time.strfttime('1988-03-03 11:11:11', '%Y-%m-%d %H:%M:%S')
timestamp = time.mktime(struct_time) + 7 * 86400
print(timestamp)

# format string <--  struct_time <-- timestamp
res = time.strfttime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
print(res)


#random

import random
random.rand()    # (0,1) float
random.randint(1,3) # [1,3]
random.randrange(1,3) # [1,3]
random.uniform(1,3) # (1,3) float
item [1,3,5,7,9]
random.shuffle(item) #打亂item的順序
```

```python
import sys

# python run.py 1 2 3
print(sys.argv) # ['run.py','1','2','3']
```

Day 23 

```python
# 序列化: 把內存的數據類型轉換成一個特定的格式的內容
# 該格式可以用來存儲或者傳輸給其他平台使用

# 內存的數據類型 --> 序列化 --> 特定的格式 (Json)

import json

res = json.dumps(True) 
print(res) # true

json_res = json.dumps([1,"aaa", True]) # 序列化
print(json_res) # [1,"aaa", true]  (str)

l = json.loads(json_res) # 反序列化
print(l) # [1,"aaa", True]  (list)

# 將序列化的結果寫入文件
with open('test.json',mode='wt',encoding='utf-8') as f:
  json.dump([1,'aaa',True], f)


# 從文件讀取json格式，並反序列化
with open('test.json',mode='rt',encoding='utf-8') as f:
  l = json.load(f)
  print(l)
  
# json格式只能兼容所有語言通用的數據類型，不能識別某一語言的獨有類型

```

```python
'''
hash: sha1, sha256
傳入內容一樣得到的hash就一樣
不能由hash反解回原來的密碼
經由一樣的hash算法出來的hash值長度是一樣的
'''
import hashlib
m = hashlib.sha256('hello'.encode('utf-8'))
res=m.hexdigest()
print(res)

# 猜密碼
cryptograph='2132sdsdsdwedfereer'

passwd = [
    'alex123',
    'alex2222',
    'alex5566'
]
dic= {}

for p in passwds:
    res = hashlib.md5(p.encode('utf-8'))
    dic[p]=res.hexdigest()
print(dic)

for k,v in dic.items():
    if v == cryptograph:
        print('password is %s' %k)
        break

# 密碼加鹽

        

```

Day 27

物件是一個容器，用來盛放資料和功能

```python
'''
物件是一個容器，用來盛放資料和功能
類也是一個容器，該容器用來存放物件共有的資料和功能 
'''
# 先定義類
# 類在定義階段就運行了，會產生一個類的名稱空間
class Student:
    # 資料
    stu_school = 'NTHU'
    
    # 初始化的函數，在類調用時會自動執行
    def __init__(obj,x,y,z):
        obj.stu_name=x
        obj.stu_age=y
        obj.stu_gender=z
    
    # 功能
    def tell_stu_info(obj):
        print(obj.stu_name)
        
    def set_info(obj,x,y,z):
        obj.stu_name=x
        obj.stu_age=y
        obj.stu_gender=z

# 屬性訪問的語法
print(Student.stu_school)
print(Student.set_info)


# 調用類產生對象(實例化)
# 讓類跟物件產生關聯
# 1. 先產生一個空物件
# 2. python會自動調用類中的__init__方法，然後將空對象傳入__inin__的參數中
# 3. 返回初始化好的對象

stu1_obj = Student('Ian',18,'male')  #  Student.__init__(stu1_obj, 'Ian',18,'male') 
stu2_obj = Student('Tom',20,'male')

print(stu1_obj.stu_name)
print(stu1_obj.stu_age)
print(stu1_obj.stu_gender)
print(stu1_obj.stu_school)

Day 30
```

```python
'''
mixins機制:在多繼承背景下盡可能地提升多繼承的可讀性
'''
class Vehicle:
  pass
class FlyableMixin:
  pass

class Aircraft(FlyableMixin, Vehicle):
  pass

class Helicopter(FlyableMixin, Vehicle):
  pass
class Car(Vehicle):
  pass


# 子類要用到父類的init方式

# 1
class People():
  def __init__(self, name, age):
    self.name = name,
    self.age = age

class Teacher(People):
  def __init__(self, name,age,level):
    People.__init__(self,name,age,sex)
    
    self.level = level
    
teacher_obj = Teacher('Ian', 18, 'high')

# 2: super 會得到一個對象，該對象會參照目前類的mro,去當前的父類找屬性
class People():
  def __init__(self, name, age):
    self.name = name,
    self.age = age

class Teacher(People):
  def __init__(self, name,age,level):
    super().__init__(name,age,sex)
    
    self.level = level
    
teacher_obj = Teacher('Ian', 18, 'high')


# 多型: 同一種事物有多種型態
import abc
class Animal(metaclass=abc.ABCMeta): #統一所有子類別的標準
  
  @abc.abstractmethod  # 強制子類別一定要有say方法
  def say(self):
    print("voice")

# obj = Animal() 不能實例化抽象類


class People(Animal):
  def say(self):
    super().say()
    print('ahahahah')
    
class Dog(Animal):
  def say(self):
    super().say()
    print('wangwang')
    
obj1 = People()
obj2 = Dog()
obj3 = Pig()

obj1.say()
obj2.say()
obj3.say()
    

'''
綁定方法: 可以將調用者本身以第一個參數傳入
1. 綁定給對象的方法
2. 綁定給類的方法
'''
import settings
class Mysql:
  def __init__(self,ip,port):
    self.ip = ip
    self.port = port
  
  @classmethod # 將下列函數裝飾成綁定給類的內容，通常用來造物件
  def from_conf(cls):
    return cls(settings.IP, settings.PORT)
    
obj1 = Mysql('127.0.0.1', 3306) # 傳入物件的方式來造物件

obj2 = Mysql.from_conf() # 傳入類的方式來造物件

'''
非綁定方法: 靜態方法
調用者可以是類或物件
''' 

class Mysql:
  def __init__(self,ip,port):
    self.ip = ip
    self.port = port
    
  @staticmethod 
  def create_id():
    import uuid
    return uuid.uuid4()
    
obj1 = Mysql('127.0.0.1', 3306) # 傳入物件的方式來造物件

Mysql.create_id()
obj1.create_id()

=======
Day 24 

​```python
'''
將封裝的屬性進行隱藏操作(在屬性名前加__前綴)
'''
class Foo:
    __x = 1
    
    def __f1(self):
        print('aa')
    def f2(self): 
        print(self.__x)
        
print(Foo.__x) # 在類的外面調用不到
obj = Foo()
obj.f2()  # 這樣可以調用得到
----------------------------------------
class Foo:
    __x = 1
    
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
obj = Foo('egon', 18)
print(obj.name, obj.age) # 調用不到
```

Day29

```python
'''
property是一個裝飾器
'''
class People:
    def __init__(self, name, height, weight):
        self.name = name,
        self.weight = weight,
        self.height = height
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)
        
        
obj1 = People('egon', 180, 70)
obj1.bmi()
obj1.bmi  # 加了property讓他看起來很像是變數



class People:
    def __init__(self, name):
        self.__name = name
    def get_name(self): 
        return self.__name
    def set_name(self, val):
        if type(val) is not str:
            print('fail')
            return
        self.__name = val
    def del_name(self):
        print('cannot delete')
    
    name = property(get_name. set_name, del_name)
        
obj1 = People('egon')
print(obj1.get_name())
obj1.set_name('EEE')
print(obj1.get_name())
# 加了property讓他看起來很像是變數
obj1.name # get_name
obj1.name = 'EGON'  # 可以set_name
del obj1.name   # 不能刪除


# 3
class People:
    def __init__(self, name):
        self.__name = name
        
    @property    
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self, val):
        if type(val) is not str:
            print('fail')
            return
        self.__name = val
        
    @name.deleter
    def name(self):
        print('cannot delete')

        
obj1 = People('egon')
# 加了property讓他看起來很像是變數
obj1.name # get_name
obj1.name = 'EGON'  # 可以set_name
del obj1.name   # 不能刪除
```

```python
'''
python 支援多繼承
如果沒有繼承東西, 默認繼承object
繼承用來解決類與類之間代碼冗餘問題
優點: 子類可以同時遺傳多個父類<的屬性,最大限度的重用代碼
缺點: 
違背人的思維習慣: 繼承表達的是一種 "是" 的關係
可讀性變差(要找很多個父類才找得到想要的變數或功能)
不建議使用多繼承，會造成菱形問題
'''
class Parent1:

class Parent2:

class Sub1(Parent1):
    
class Sub2(Parent1,Parent2):
```

Day 33

Python是動態語言，反射(reflection)機制是動態語言的關鍵

反射是指在程式運行狀態中，對於任何一個類，都知道這個類的所有屬性與方法

對象則能夠調用他的任意方法和屬性

實現反射的步驟

1. 先通過dir，啥看某一個對象下可以.出哪些屬性
   `print(dir(obj))`
2. 可以通過字串反射到真正的屬性上，得到屬性值
   obj.'name' 

四個內置函數的使用: 通過字串來操作屬性值

1. hasattr(): print(hasattr(obj, 'name'))
2. getattr(): print(getattr(obj, 'name'))
3. setattr(): print(getattr(obj, 'name','Ian'))
4. delattr() delattr(obj,'name')  print(obj.__dict__)

內置方法: 在類的內部，以_ _開頭，以_ _ _結尾，在某些情況下會自動調用

```python
'''
__str__: 在print時自動觸發
__del__: 在清理對象時觸發
'''

# 元類 ---> 實例化 ---> 類 (People)---> 實例化 --> object (obj)

print(type(People))

'''
class關鍵字造類的步驟
類有三大特性
1.類名
2.類的父類
3.執行類體代碼拿到類的名稱空間
exec(class_body,{},class_dic)
4.調用元類
'''
```

