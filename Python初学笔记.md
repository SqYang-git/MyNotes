# Python初学笔记

## 变量

赋值操作里,等号左边的会先被视作变量,等号右边的是变量被赋的值(不必须是数字)

变量替换后无法找回之前的值

e.g.1:前任与现任的手机号储存(doge)

```python
my_love = 13766666666
my_ex = my_love
my_love = 15066666666
```

e.g.2:批量化greet

```python
hi = "您好,吃了吗,"
print(hi + "Alice")
print(hi + "Bob")
```

变量名:文字/数字/下划线;不占用关键操作名(即打出来不是高亮显示的)

建议:英文,字母全部小写,下划线分隔(下划线命名法)

---

------

## 注释#

单行前加`#`(也可实现代码跳过执行)

多行快速注释:选中 com /(重复操作撤销注释)

也可由三引号`'''blabla'''`/`"""blabla"""`进行多行注释

---

------

## 数据类型

------

### 字符串str

#### 长度len

`len()`可给出字符串长度(空格,数字和符号均占1长度;完整的转义符占1长度)
字符串后加`[n]`可得到第n个字符(从0开始数)

#### 打印print

1. 字符串(""包裹的部分)连接:""+"",e.g.

   ```python
   print("Hello" + " world" + "!")
   ```

   效果为`Hello world!`

2. 单双引号转义
   引号包引号运行会出错,Python引号配对最近的引号,解决办法:

   1. 内外分单双

      ```python
      print('He said "good!"')
      ```

   2. 字符串引号前加\转译

      ```python
      print("He said\"Let\'s go!\"")
      ```

3. 换行

   ```python
   print("Hello!\nHi!")
   ```

   效果为

   ```
   Hello!
   Hi!
   ```

4. 三引号跨行字符串

   ```python
   print('''君不见，黄河之水天上来，奔流到海不复回。
   君不见，高堂明镜悲白发，朝如青丝暮成雪。
   人生得意须尽欢，莫使金樽空对月。
   天生我材必有用，千金散尽还复来。
   烹羊宰牛且为乐，会须一饮三百杯。
   岑夫子，丹丘生，将进酒，君莫停。
   与君歌一曲，请君为我倾耳听。
   钟鼓馔玉不足贵，但愿长醉不复醒。
   古来圣贤皆寂寞，惟有饮者留其名。
   陈王昔时宴平乐，斗酒十干恣欢谑。
   主人何为言少钱，径须沽取对君酌。
   五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。''')
   ```

   此时换行不被作为代码语句结束,而是内容的换行

#### 切片split

```python
str_1.split( , 1 )  
```

第一个空作为切片标志的分隔符,默认为空字符(Space,`\n`,`\t`)

如只需在一种空字符处分割,填`" "`,`"\n"`,`"\t"`

第二个空填分割次数,默认为-1,即全部分割

------

### 整数int与浮点数float

#### 数值运算

基本运算优先级:`()`>`**`>`*`,`/`>`+`,`-`
`%`求前者除以后者的余数
`//`求前者除以后者的结果(int)
e.g.一元二次求根器

```python
import math
a = 1
b = 9
c = 20
delta = b ** 2 - 4 * a * c
print((- b + math.sqrt(delta)) / (2 * a))
print((- b - math.sqrt(delta)) / (2 * a))
```

------

### 布尔类型bool

------

### 空值类型NoneType

需定义变量但还不知道值时可先行定义为`None`

`type()`可返回对象类型

---

------

## 输入input

e.g.1

```python
user_age=int(input("请输入您的年龄: "))
print("您十年后会是"+str(user_age+10)+"岁")
```

此时`user_age`会被视为str类型,无法进行数学运算需要使用`int()`函数

(同理`float()`,`str()`可转化出浮点和字符串,后者在需要`print`时有用)

e.g.2

```python
#BMI=weight/(height**2)
weight=float(input("请输入您的体重(单位:kg): "))
height=float(input("请输入您的身高(单位:m): "))
BMI=weight/(height**2)
print("您的BMI为:"+str(BMI))
```



---

------

## 条件语句

```python
if [条件1]:
  if [条件1_1]:
		[执行语句1_1]
  else:
    [语句1_2]
elif [条件2]:
		[执行语句]
else:
		[执行语句]
```

### 比较运算符

输出bool,注意应为数字比较

`==`是否相等,`!=`是否不等,`>`,`>=`,`<`,`<=`常见

如条件1满足,则不会继续运行条件2,即使其为真

e.g.

```python
#BMI=weight/(height**2)
weight=float(input("请输入您的体重(单位:kg): "))
height=float(input("请输入您的身高(单位:m): "))
BMI=weight/(height**2)
print("您的BMI为:"+str(BMI))
if BMI<=18.5:
  	print("您偏瘦")
elif 18.5<BMI<=25
		print("您体型正常")
elif 25<BMI<=30
		print("您偏胖")
else
		print("该减肥力")
```

### 逻辑运算符

`and`:均为`True`才会返回`Trued`

`or`:有一个为`True`则会返回`True`

`not`:使布尔值反转

优先级:`not`>`and`>`or`,可以通过括号改变运算顺序

用逻辑运算代替嵌套有时能使条件运算更加优雅

```python
if (house_work_count › 10 and red_envelope_count › 1 and
shopping_count> 4 and not has_been_angry):
  print（"摩拳擦掌等待Switch！"）
else:
  print（"Switch随风散去..."）
```

---

------

## 列表list

e.g.

```python
list1=["键盘","键帽","显示器"]
list1.append("显示器")
list1.remove("键帽")
list1.append(66.6)
list1.append(True)
list1.append(None)#各种类型的数据
print(list1)
len(list1)#求长度
print(list1[0])
list1[0]="音响"#索引覆盖
print(sorted(list1))#打印排序后的列表
```

```python
#对数字类型的列表
num_list=[1,13,-7,2,96]
print(max(num_list))#打印列表里的最大値
print(min(num_list))#打印列表里的最小値
print(sum(num_list))#打印列表里数据的和
```

`list`类型被`.append`改变,无需再次赋值

区分:方法`对象.方法名(...)`与函数`函数名(对象)`

---

------

## 字典dict

用于储存key:value对,e.g.

```python
contacts={"Alice":"13700000000",
         "Bob":"13700000001"}
print(contacts["Alice"])#给出key对应的value
contacts["Charlie"]="18600000000"#添加/覆盖key:value
print("Alice"in contacts)#判断key是否存在,返回bool
del contacts["Bob"]#删除key
len(contacts)#获得dict长度
```

注:key只能是不可变数据类型,如需多个确认方式,使用元组tuple作为key

```python
tuple1=("Alice","Bob")
```

tuple不可以使用`.apped`或`.remove`

```python
dict1.keys()#返回所有key
dict1.values()#返回所有value
dict1.items ()#返回所有key:value
```

---

------

## for 循环

```python
for 变量 in 可迭代对象
	#对可迭代对象做一些操作
	#变量会被依次赋值为可迭代对象里的每个元素
```

e.g.

```python
temp_dict={"001":36.1,"002":38.4,"003":37.2}
for staff_id,temp in temp_dict.items():
  if temp>=38:
    print(staff_id)
```

结合`range(起始值,结束值,步长)`(仅放一个值时默认起始值为0;结束值不算在内)

```python
tot=0
for i in range(1,101):
  tot=tot+i
print(tot)
```

---

------

## while循环

```python
print("芝士求平均值的程序")
total=0
count=0
num_input=print("请输入数字或quit:")
while num_input != "quit":
  num=float(num_input)
  total+=num#与total+num=total同
  count+=1
  num_input=print("请输入数字或quit:")
if count==0:
  result=0
else:
  result=total/count
print("您输入的数字平均值为"+str(result))
```

---

------

## 格式化字符串

### format方法

e.g.格式化祝福

```python
contacts=["老余","老林","老陈","老曾","老李","老张"]
year="虎"
for name in contacts:
  message_content='''
律回春渐,新元肇启.
新岁甫至,福气东来.
金{0}贺岁,欢乐祥瑞.
金{0}敲门,五福临门.
给{1}及家人拜年啦!
新春快乐,{0}年大吉!
'''.format(year,name)
```

### f-字符串

```python
contacts=["老余","老林","老陈","老曾","老李","老张"]
year="虎"
for name in contacts:
  message_content=f'''
律回春渐,新元肇启.
新岁甫至,福气东来.
金{year}贺岁,欢乐祥瑞.
金{year}敲门,五福临门.
给{name}及家人拜年啦!
新春快乐,{year}年大吉!
'''
```

---

------

## def定义函数

定义函数时,代码不会被执行,仅调用函数时被执行

```python
def calculate_sector(angle,radius):
  #接下来是一些定义函数的代码
  area=angle/360*π*radius**2
  print(f"此扇形面积为:{area:.9f}")
angle=float(input("请输入圆心角: "))
radius=float(input("请输入半径: "))
calculate_sector(angle,radius)
```

返回计算结果用到`return`

```python
def calculate_BMI(weight,height):
    BMI=weight/height**2
    if BMI<=18.5:
        category="偏瘦"
    elif 18.5<BMI<=25:
        category="正常"
    elif 25<BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的体重:{category}")
    return BMI
weight=float(input("请输入体重: "))
height=float(input("请输入身高: "))
result=calculate_BMI(weight, height)
print(result)
```

---

------

## 引入模块

### import

```python
import statistics
print(statistics.median([19,-5,36]))
print(statistics.mean([19,-5,36]))
print(statistics.variance([19,-5,36]))
```

从同一模块引入多个函数时代码偏长

### from...import...

```python
from statistics import median,mean,variance
print(median([19,-5,36]))
print(mean([19,-5,36]))
print(variance([19,-5,36]))
```

精简代码,引入模块里需要的函数

### from...import *

```python
from statistics import *
print(median([19,-5,36]))
print(mean([19,-5,36]))
print(variance([19,-5,36]))
```

精简代码,引入模块里所有函数(不推荐,可能与其他模块的函数冲突)

查看引入函数源代码:com click

引入第三方模块须先行安装:终端pip install ~

---

------

## Object-Oriented Programming

了解对象属性Attribute,从而定义类class来创建对象,参数更少,程序逻辑更清晰

将方法Method与类class绑定(可看作class里的函数)

### 类的创建:

```python
class NameOfClass:#用Pascal命名法
  def __init__(self,name,age):#定义类的代码括号内放参数
    self.name=name
    self.age=age
  def barking(self):
    print(self.name+"在barking")
  def thinking(self,content):
    print(self.name+"的脑子宕机了")
object1=NameOfClass("yxy",17)
print(f"{object1.name}的年龄是{object1.age}岁")
object1.barking()
object1.thinking("吃什么")
```

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"力学": 0, "电磁学": 0, "热学": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grade(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩为:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


yang = Student("yxy", "2400011308")
print(yang.name)
yang.set_grade("电磁学", 90)
print(yang.grades)
yang.print_grade()
```

### 类的继承:

调用方法时优先看子类有无该方法.没有则寻找父类的同名方法

```python
#创建父类Mammal
class Mammal:
  def __init__(self,name,sex):
    self.name=name
    self.sex=sex
    self.num_eyes=2
	
  def breath(self):
    print(self.name+"在呼吸")
    
  def poop(self):
    print(self.name+"在拉屎")
    
#创建子类Human
class Human(Mammal):
  def __init__(self):
    super().__init__(name,sex)#调用父类的构造函数
    self.has_tail=False
    
	def read(self):
    print(self.name+"在阅读")
  
#创建子类Cat
class Cat(Mammal):
  def __init__(self):
    super().__init__(name,sex)
    self.has_tail=True
    
  def scratch_sofa(self):
    print(self.name+"在抓沙发")
```

---

------

## 读文件read

```python
f=open("filepath","r",encoding="utf-8")
#后两个不写会默认为"r""utf-8"
print(f.read(10))
#python会记忆,二次使用返回空字符串
#限制字节数可以防止内存爆掉

print(f.readline())
#还可以自动判断是否读完
line=f.readline()#读第一行
while line !="":#是否为空字符串
  print(line)#不空则打印
  line=f.readline#读下一行
  
print(f.readlines)
#读取全部文件内容,返回由每行组成的字符串列表(包括换行符)
#优雅的打印出来
lines=f.readlines()#把每行内容储存到列表里
for line in lines:#遍历每行内容
print(line)#打印当前行

f.close()
```

另一种:

```python
with open("filepath") as f:
  #print
  #此时无需close
```

---

------

## 写文件write/add

只写模式:

```python
with open("filepath","w",encoding="utf-8") as f:
  #如文件存在,则会被清空
  #如文件不存在,则会被创建
  
  f.write("Hello!\n")#需要手动添加换行符
  f.write("Yipeee!")
```

追加模式:

```python
with open("filepath","a",encoding="utf-8") as f:
  f.write("\n Hello!\n")
  f.write("Yipeee!")
```

读写模式:

```python
with open("filepath","r+",encoding="utf-8") as f:
  #此时read和write的方法都可以调用,且write为追加
```

---

------

## Python异常处理

```python
try:
  #可能会报错的代码
except 错误名称:
  #如发生错误执行的操作
```

e.g.

```python
def calculate_BMI(weight,height):
    BMI=weight/height**2
    if BMI<=18.5:
        category="偏瘦"
    elif 18.5<BMI<=25:
        category="正常"
    elif 25<BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的体重:{category}")
    return BMI

try:
  weight=float(input("请输入体重: "))
  height=float(input("请输入身高: "))
  result=calculate_BMI(weight, height)
except ValueError:
  print("输入不为合理数字,请重新运行程序,并输入正确的数字")
except ZeroDivisionError:
  print("身高不能为零,请重新运行程序,并输入正确的数字")
except:
  print("发生了未知错误,请重新运行程序")#这个需要写到最后
else:
  print(result)
finally:
  print("程序结束运行")
```

---

------

## Python测试

断言`assert`后跟布尔表达式,求值为`False`则显示`AssertionError`并终止程序运行

unittest是一个python自带单元测试库.测试代码一般应放于独立文件.

被测试文件与测试文件位于同一文件夹下时,

```python
import unitest
from filename import classname/functionname
```

e.g.

被测试代码:

```python
def adder(x,y):
  return x+y
```

测试代码:

```python
import unitest
from my_caculator import my_adder

class TestMyAdder(unitest.Testcase):
  #定义测试用例(该类下的一个方法)
  def test_negative_with_positive(self):#必须以test_开头
    self.assertEqual(my_adder(5,3),8)
  def test_negative_with_positive(self):
    self.assertEqual(my_adder(-5,3),-2)
```

之后在编辑器终端输入`python -m unittest`,则会自动搜索所有继承了unittest库里TestCase类的子类,运行他们所有以`test_`开头的方法,然后展示测试结果(测试成功):

```tex
..
---------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

如测试不通过,`.`会变成`F`,并详细展示那个文件下的那个方法造成测试失败,以及失败原因

------

unitest.Testcase类的常见测试方法(对应的取反方法在assert后加Not即可,True例外变为False)

本质上`assertTrue`万能,但方法更具针对性则失败原因越详细

```python
assertEqual(A,B)#类似于assert A==B
assertTrue(A)#类似于assert A is True
assertIn(A,B)#类似于assert A in B
```

---

---

## 高阶和匿名函数

e.g.多功能计算器

```python
def calculate_and_print(num,calculator):
  #高阶函数:把函数作为高阶函数的参数
  #注意只输入函数名而不带括号,否则函数将被调用,传入的为执行结果
  result=calculator(num)
  print(f"""
  |数字参数|{num}|
  |计算结果|{result}|""")
  
def calculate_square(num):
  return num*num

def calculate_cube(num):
  return num*num*num

def calculate_plus_10(num):
  return num+10
#调用示例
calculate_and_print(3,calculate_square)
```

