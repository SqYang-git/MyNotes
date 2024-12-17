m = int(input())  # 最⼤位数
n = int(input())  # 正整数数量
nums = input().split()


def f(string):  # 得到整数形式
    if string == '':
        return 0
    else:
        return int(string)


for i in range(n):  # 冒泡排序,可以证明l在拼接意义上有序
    for j in range(n - 1 - i):
        if nums[j] + nums[j + 1] > nums[j + 1] + nums[j]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

weight = []  # 排序后每个元素的长度
for num in nums:
    weight.append(len(num))
# dp部分
# 在前i个元素中选择,不超过j位的最大可能数值
dp = [[''] * (m + 1) for _ in range(n + 1)]
# 初始化
for k in range(m + 1):
    dp[0][k] = ''
for q in range(n + 1):
    dp[q][0] = ''
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if weight[i - 1] > j:  # 如果超位数
            dp[i][j] = dp[i - 1][j]
        else:  # 可以选第 i 个，也可以不选
            dp[i][j] = str(max(f(dp[i - 1][j]), int(nums[i - 1] + dp[i - 1][j - weight[i - 1]])))
print(dp[n][m])
