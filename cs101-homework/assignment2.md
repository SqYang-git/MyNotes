# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==杨馨尧,物理学院==

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A

##### 代码

```python
count = 0
for i in range(5):
    j = input().find("1")
    if j != -1:
        count += abs(j-4)/2+abs(i-2)

print(f"{count:.0f}")

```

代码运行截图 ==（至少包含有"Accepted"）==

![](https://p.ipic.vip/9bbojr.png)

### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A

##### 代码

```python
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        step = b - (a % b)
        print(step)

```

代码运行截图 ==（至少包含有"Accepted"）==

![](https://p.ipic.vip/nhir3e.png)

### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A

##### 代码

```python
n = int(input())
a = list(map(int, input().split()))
crime = 0
officers = 0
for i in a:
    if i == -1:
        if officers == 0:
            crime += 1
        else:
            officers -= 1
    if i > 0:
        officers += i
print(crime) 

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://p.ipic.vip/nhir3e.png)

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/

##### 代码

```python
def remain(L, M, regions):
    trees = [1] * (L + 1)
    for start, end in regions:
        for i in range(start, end + 1):
            trees[i] = 0
    remaining_trees = sum(trees)
    return remaining_trees


L, M = map(int, input().split())
regions = []
for _ in range(M):
    a, b = map(int, input().split())
    regions.append((a, b))
result = remain(L, M, regions)
print(result)

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://p.ipic.vip/me5bn4.png)

### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60

##### 代码

```python
def is_daffodil(num):
    i = int(num/100)
    j = int(num/10 - 10 * i)
    k = int(num - 100 * i - 10 * j)
    if i ** 3 + j ** 3 + k ** 3 == num:
        return True


couple = input().split()
a = int(couple[0])
b = int(couple[1])
daffodils = []
for m in range(a, b + 1):
    if is_daffodil(m):
        daffodils.append(m)

if len(daffodils) == 0:
    print("NO")
else:
    m = len(daffodils)
    for n in range(m-1):
        print(daffodils[n], end=" ")
    print(daffodils[m-1])

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://p.ipic.vip/udgxcj.png)

### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/

##### 代码

```python
import math

while True:
    n = int(input())
    if n == 0:
        break
    max_time = float("inf")
    for _ in range(n):
        speed, time = map(int, input().split())
        if time < 0:
            continue
        arrival_time = math.ceil((4500 / speed) * 3.6 + time)
        max_time = min(max_time, arrival_time)

    print(max_time)

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://p.ipic.vip/lw8km3.png)

## 2. 学习总结和收获

中秋前后太摆烂了💦,每日没能全部跟着做,这几天各种任务进入良性循环,也有时间在做题AC的基础上多考虑一下优化算法的问题:拿自己的代码和AI的对比,AI更优但我无法理解的话会去问之前学信竞的外校同学,尽管他学C++,仍能在算法上给我不少指导(信竞人还是很在乎runtime的).现在也算是被AI教出来了,总想着def再调用(笑)