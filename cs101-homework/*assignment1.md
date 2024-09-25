# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==杨馨尧_物理学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：



##### 代码

```python
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'Y'
            else:
                return 'N'
        else:
            return 'Y'
    else:
        return 'N'


year = int(input())
result = is_leap_year(year)
print(result) 

```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-10 19.16.38](https://p.ipic.vip/ta0sh6.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：



##### 代码

```python
def calculate_animals(num_legs):
    if num_legs % 2 != 0:
        return 0, 0
    if num_legs % 4 == 0:
        min_animals = num_legs // 4
    else:
        min_animals = num_legs // 4 + 1

    max_animals = num_legs // 2
    return min_animals, max_animals


num_legs = int(input())

min_animals, max_animals = calculate_animals(num_legs)
print(min_animals, max_animals)

```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-10 19.18.10](https://p.ipic.vip/krheg1.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：



##### 代码

```python
def max_dominoes(M, N):
    return (M * N) // 2


M, N = map(int, input().split())
print(max_dominoes(M, N))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-10 19.21.11](https://p.ipic.vip/pdu0l3.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：



##### 代码

```python
n, m, a = map(int, input().split())
width = (n + a - 1) // a
height = (m + a - 1) // a
total = width * height
print(total)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-10 19.40.36](https://p.ipic.vip/iux0h1.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：



##### 代码

```python
str1 = input()
str2 = input()
str1_lower = str1.lower()
str2_lower = str2.lower()
if str1_lower < str2_lower:
    print("-1")
elif str1_lower > str2_lower:
    print("1")
else:
    print("0")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="https://p.ipic.vip/qqumrm.png" alt="截屏2024-09-10 20.14.05"  />



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：



##### 代码

```python
num = int(input())
count = 0
for i in range(num):
    sum1 = list(map(int, input().split()))
    if sum(sum1) >= 2:
        count += 1

print(count)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-10 20.32.42](https://p.ipic.vip/w0kpqf.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

额外练习:
200B. Drinks
4A. Watermelong
158A. Next Round
236A. Boy or Girl

从零基础了解了python语法,并学会了用AI工具辅助学习,以及善用搜索💦





