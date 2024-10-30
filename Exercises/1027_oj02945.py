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
