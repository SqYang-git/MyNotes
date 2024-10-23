# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>杨馨尧 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

代码：

```python
num = 1
while True:
    p, e, i, d = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1]:
        break
        
    count = d+1
    while (count-p) % 23 != 0 or (count-e) % 28 != 0 or (count-i) % 33 != 0:
        count += 1

    print(f"Case {num}: the next triple peak occurs in {count - d} days.")
    num += 1

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/9z88a2.png)

### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

代码：

```python
p = int(input())
cost = list(map(int, input().split()))
cost.sort()

gap = 0
left = 0
right = len(cost) - 1

while left <= right:
    if cost[left] <= p:  # 继续制作
        p -= cost[left]
        gap += 1
        left += 1
    else:
        if left == right:  # 钱不够,但是没得做了
            break
        p += cost[right]  # 卖图纸
        right -= 1
        gap -= 1
        if gap < 0:  # 任一时刻差距不能为负(题干要求)
            gap = 0
            break

print(gap)

```

代码运行截图 ==（至少包含有"Accepted"）==

![](https://p.ipic.vip/yizgcb.png)

### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：`enumerate`第一次见💦

代码：

```python
n = int(input())
list_t = list(map(int, input().split()))
indexed_list_t = list(enumerate(list_t))  # 给出位置
indexed_list_t.sort(key=lambda x: x[1])  #按值排序
for i, t in indexed_list_t:
    print(i+1, end=" ")  # 注意i从0开始
print()  # 分行
list_t.sort()
t = sum((n-1-i) * list_t[i] for i in range(n))/n
print(f"{t:.2f}")

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/2y1s39.png)

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

代码：

```python
def FormHabbToTzolkin(int_day, month, int_year):
    list_Habb_month = ["pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", "yax", "zac", "ceh", "mac",
                       "kankin", "muan", "pax", "koyab", "cumhu", "uayet"]
    list_Tzolkin = ["imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", "ok", "chuen", "eb",
                    "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"]
    num = int_day + 1 + list_Habb_month.index(month) * 20 + int_year * 365  # 总天数
    Year = num // 260 - 1 if num % 260 == 0 else num // 260  # 注意某一年恰好满时
    num = num % 260  #剩下天数,放便处理
    NameOfTheDay = list_Tzolkin[num % 20 - 1]  # 注意为20倍数时实为“ahau”,错位
    date = 13 if num % 13 == 0 else num % 13  # 注意整13倍数时输出“13”
    return str(date) + " " + NameOfTheDay + " " + str(Year)


n = int(input())
ans = [f"{n}"]
for i in range(n):
    day, month, year = input().split()
    int_day = int(day[:len(day)-1])
    int_year = int(year)
    ans.append(FormHabbToTzolkin(int_day, month, int_year))
print("\n".join(ans))

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/989szq.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

代码：

```python
n = int(input())
segments = []
for i in range (n):
    x, h = map(int, input().split())
    segments.append([x-h, x+h])

count = 1  # 第一个必然可砍
left = (segments[0][0] + segments[0][1]) // 2  #左端为第一个树根
for i in range(1, n):
    if segments[i][0] > left:  # 可向左倒
        count += 1
        left = (segments[i][0] + segments[i][1]) // 2  #更新左端为树根
    elif i == n-1:  #最右侧必然可倒,先拿出来防止下一个越界)
        count += 1
    elif segments[i][1] < (segments[i+1][0] + segments[i+1][1]) // 2:  #可向右倒
        count += 1
        left = segments[i][1]
    else:  #倒不了一点
        left = (segments[i][0] + segments[i][1]) // 2

print(count)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/wl7jrz.png)

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

代码：

```python
num = 0  # 情况编号
while True:
    n, d = map(int, input().split())
    if n == 0:
        break
    else:
        num += 1
        radars = []
        for i in range(n):
            x, y = map(int, input().split())
            if y <= d:
                radars.append(([x - (d ** 2 - y ** 2) ** 0.5, x + (d ** 2 - y ** 2) ** 0.5]))
        input()  # 输入空行
        if len(radars) < n:  # 存在无法覆盖的小岛
            print(f"Case {num}: -1")
        else:
            radars.sort(reverse=True)  # 左端从大到小排序
            count = len(radars)
            i = 0  # 指针(?)
            for j in range(1, n):
                if radars[i][0] > radars[j][1]:  # 无法被前一个覆盖,指针移动,换范围继续判定
                    i = j
                else:  # 可被前一个覆盖
                    count -= 1
            print(f"Case {num}: {count}")

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/09zpcx.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业题目费了不少时间(虽然都是每日选做题目)
时间投入还是不太够,未能完全跟上每日选做
最近的题目做起来都比较有收获,初步理解了双指针,了解了滑动窗口型题目等
做题还是容易忘掉一些边界的输入值,总是掉坑,感觉是之前有时图方便没有养成自己写写思路和注意点的习惯,反倒经常成为卡进度的导火索(懒导致的💦)
cheetsheet做了一点了
