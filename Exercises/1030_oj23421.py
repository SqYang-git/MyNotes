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
