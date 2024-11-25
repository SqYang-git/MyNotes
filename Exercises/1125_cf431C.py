from functools import lru_cache
modulo = 1000000007  # 取模防止结果溢出


@lru_cache(maxsize=None)  # 缓存防止重复计算
def dfs(n, b):
    # 若已达一个末端,且当前路径上最大权重等于d,记录一个结果
    if n == 0 and b >= d:
        return 1
    # 若超出路径加权限制,返回0
    if n < 0:
        return 0
    # 初始化结果
    ans = 0
    # 对k条分支进行搜索
    for i in range(1, k+1):
        ans = (ans + dfs(n-i, max(b, i))) % modulo
    return ans


n, k, d = map(int, input().split())
print(dfs(n, 0))
