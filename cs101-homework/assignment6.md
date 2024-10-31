# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>物理学院,杨馨尧</mark>

## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：搜了下使步骤最少的解决思路才做出来💦,见代码注释,本质上还是递归

代码：

```python
answers = []


def move(height, start, end, buffer):
    # 如果没有盘子，直接返回
    # 如果有盘子
    if height >= 1:
        # 将上面的盘子从 start 移到 buffer,end作为辅助
        move(height - 1, start, buffer, end)
        # 将最下面的盘子移到 end
        answers.append(f"{start}->{end}")
        # 将 buffer 上的盘子移到 end,start作为辅助
        move(height - 1, buffer, end, start)


n = int(input())
move(n, 'A', 'C', 'B')
print(len(answers))
for ans in answers:
    print(ans)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/lro8f6.png)

### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：见代码注释

代码：

```python
n = int(input())
str1 = "".join([str(i + 1) for i in range(n)])


def order_n(str1):
    ans = []
    # 字符串为空时，返回一个空字符串构成的列表
    if len(str1) == 0:
        ans.append("")
        return ans
    if len(str1) == 1:
        ans.append(str1)
        return ans
    # 遍历字符串的每一个字符
    for i in range(len(str1)):
        # 当前字符
        current = str1[i]
        # 剩余字符，排除当前字符
        remain = str1[:i] + str1[i + 1:]
        # 对剩余字符生成全排列，并加上当前字符进行组合
        for _ in order_n(remain):
            ans.append(current + " " + _)
    return ans


ans = order_n(str1)
for i in ans:
    print(i)

```

代码运行截图 ==（至少包含有"Accepted"）==

![](https://p.ipic.vip/8ud3vm.png)

### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：见代码注释

代码：

```python
# 最长递减子序列
k = int(input())
# 读取导弹高度并立即反转存储,化为最长递减子序列问题
missiles = list(reversed(list(map(int, input().split()))))
dp = [0] * k
for i in range(k):
    # 初始化“到i的最长递增子序列”的长度为1
    max_n = 1
    # 遍历当前位置i之前的位置j
    for j in range(i):
        # 若之前某个导弹j的高度小于导弹i的高度
        # 并且“到j的最长递增子序列”的长度加1大于当前的最大子序列长度
        # 更新“到i的最长递增子序列”的长度为dp[j]+1,否则仍为之前记录的最大子序列长度
        if missiles[i] >= missiles[j] and dp[j] + 1 > max_n:
            max_n = dp[j] + 1
    # 将“到i的最长递增子序列”的长度保存至dp
    dp[i] = max_n

print(max(dp))

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/nz0wkv.png)

### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：
见代码注释,这里采用的是"算法图解"中的思路,给出一个二维的item- volume表
也可采用上一问中一维dp数组,在物品较多是减少内存占用

代码：

```python
num, bag = map(int, input().split())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
# 初始化dp数组,物品为行,包容量为列
dp = [[0] * (bag + 1) for _ in range(num + 1)]
# 多加的行和列防止数组越界
for i in range(1, num + 1):
    # 对“第i件物品”,遍历包容量
    for j in range(weights[i - 1], bag + 1):
        # 如果当前容量j大于等于“第i件物品”的重量
        # 则取两种情况的最大值,即取“不装第i件物品”和“装第i件物品”的最大值
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

print(dp[num][bag])

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/kkhw8m.png)

### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：见代码注释,通过==递归==给出92种结果

代码：

```python
answers = []


# 定义递归函数queens
def queens(ans, length):
    for i in range(1, 9):
        # 在同一行,不可放置
        if str(i) in ans:
            continue
        # 在同一斜线,不可放置
        if sum(abs(i - int(ans[j])) == length - j for j in range(length)):
            continue
        else:
            # 若已经完成一个方案
            if length == 7:
                answers.append(ans + str(i))
            # 若未完成方案,加入当前合法位置到ans末尾,继续递归
            else:
                queens(ans + str(i), length + 1)


# 从空字符串开始递归得到所有放置方案
queens("", 0)

n = int(input())
for _ in range(n):
    sequence = int(input()) - 1  # 注意列表编号
    print(answers[sequence])

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://p.ipic.vip/i09uc3.png)

### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：29号的选做没写💦,写作业的时候恰好CF炸了,只好先留着后面写

代码：

```python

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>



## 2. 学习总结和收获

因为每日选做停摆了,中间就做了两道文计的简单题,所以(算是)第一次写dp,向往年答案和通义学习了不少😭(什么时候我能机械飞升(x))

好在能用自己贫瘠的语法储备写出看得懂的答案😇
