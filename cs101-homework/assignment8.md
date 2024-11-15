# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：想清楚计数方式即可

代码：

```python
n, m = map(int, input().split())
map1 = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if map1[i][j] == 1:
            count += 4
            if i > 0 and map1[i-1][j] == 1:
                count -= 2
            if j > 0 and map1[i][j-1] == 1:
                count -= 2
print(count)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/tnzhcp.png)

### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：递归,把上一个矩阵加上一个值后安在里面(考虑"旋转"如何实现)

代码：不太熟LC,图省事直接用oj写了

```python
def rotmatrix(n):
    if n == 1:
        return [[1]]
    buffer = rotmatrix(n - 1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[0][i] = i + 1
    for i in range(1, n):
        result[i][n - 1] = n + i
    for i in range(1, n):
        for j in range(n - 1):
            result[i][j] = buffer[n - 1 - i][n - 2 - j] + 2 * n - 1
    return result


n = int(input())
matrix = rotmatrix(n)
for row in matrix:
    print(' '.join(map(str, row)))

```

代码运行截图 ==（至少包含有"Accepted"）==

![](https://p.ipic.vip/96a3z3.png)

### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：朴实的滑动窗口,注意不要越界

代码：

```python
d = int(input())
n = int(input())
street = []
for _ in range(1025):
    street.append([0] * 1025)
for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(max(0, x-d), min(1025, x+d+1)):
        for j in range(max(0, y-d), min(1025, y+d+1)):
            street[i][j] += k

count = 0
max_value = 0
for i in range(1025):
    for j in range(1025):
        if street[i][j] > max_value:
            max_value = street[i][j]
            count = 1
        elif street[i][j] == max_value:
            count += 1
print(count, max_value)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/vlrznl.png)

### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：写的比较笨拙的dp,"拦截导弹"(最长上升子序列)的升级版;因为懒得判断序列需要增/减故直接分成了两类序列分别dp,剩下的在最长上升子序列的基础上改一下判断条件即可(如对dp1,为增减增减……,故序列奇数个时要减,偶数个要增)
耗时比较长,看在我的dp水平上或许还能接受(?)

代码：

```python
n = int(input())
list_num= list(map(int, input().split()))
dp1 = [1] * n
for i in range(n):
    max_len = 1
    for j in range(i):
        if list_num[j] < list_num[i] and dp1[j] + 1 > max_len and dp1[j] % 2 == 1:
            max_len = dp1[j] + 1
        if list_num[j] > list_num[i] and dp1[j] + 1 > max_len and dp1[j] % 2 == 0:
            max_len = dp1[j] + 1
    dp1[i] = max_len
dp2 = [1] * n
for i in range(n):
    max_len = 1
    for j in range(i):
        if list_num[j] < list_num[i] and dp2[j] + 1 > max_len and dp2[j] % 2 == 0:
            max_len = dp2[j] + 1
        if list_num[j] > list_num[i] and dp2[j] + 1 > max_len and dp2[j] % 2 == 1:
            max_len = dp2[j] + 1
    dp2[i] = max_len
ans = max(max(dp1), max(dp2))
print(ans)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/0a5xi3.png)

### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：爆大数可耻但有效😋(节省点内存可以用字典).后面分情况dp就好了,`dp[i]`是取到当前数字`i`为止能得到的最大分数,分两种情况,即选择`i-1`还是`i`.若选择了`i-1`得分更高,`i`会消除,则`dp[i]=dp[i-1]`;若选择`i`得分更高,则`i-1`会消除,考虑到`i-2`之前的与`i`之和是否大于上一种情况结果来判断

代码：

```python
n = int(input())
buffer = [0] * 100001
a = list(map(int, input().split()))
for i in range(n):
    buffer[a[i]] += 1

dp = [0] * 100001
for i in range(1, 100001):
    dp[i] = max(dp[i-1], dp[i-2] + buffer[i] * i)

print(max(dp))

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/bsa99u.png)

### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：呃呃没看讲义不太知道什么是dfs,用双指针(最强最弱马),主要思路就是能多赢一点就多赢一点,赢不了时就尽量保存自身实力,消耗对方实力.

代码：

```python
while True:
    n = int(input())
    if n == 0:
        break
    TJ = list(map(int, input().split()))
    K = list(map(int, input().split()))
    TJ.sort()
    K.sort()
    profit = 0
    l1 = 0; r1 = n - 1; l2 = 0; r2 = n - 1
    # 未数尽所有马时
    while l1 <= r1:
        # 若目前最弱的马可以赛赢对方目前最弱的马,则用最弱的马赛对方最弱的马.去掉双方最弱的马
        if TJ[l1] >K[l2]:
            profit += 200
            l1 += 1
            l2 += 1
        # 若目前最弱的马不能赛赢目前对方最弱的马
        # 若目前最强的马可以赛赢对方最强的马,比先失利再得利获利更大.
        # 那么应该用最强的马赛对方最强的马.去掉双方最强的马.
        elif TJ[r1] > K[r2]:
            profit += 200
            r1 -= 1
            r2 -= 1
        else:
            # 若最强的马会输给对方最强的马,则用最弱的马赛对方最强的马,充当炮灰.失去200银元.
            if TJ[l1] < K[r2]:
                profit -= 200
            # 若最弱的马与对方最强的马实力相当,仍坚持战术,无需失去银元.
            l1 += 1
            r2 -= 1

    print(profit)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/0x0lsb.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

期中考完力,被迫达成绩点自由😭✌️

有充足精力补每日选做了(发现github仓库里传的题还不足百道💦),把greedy和dfs欠的东西补了(好像真没做过几道greedy),dp和递归再练下.

多出来时间的话看看讲义整理到cheetsheet上.

希望期末能靠计概和一众政治课结束绩点自由的状态(专绩铁定是爆了😭)
