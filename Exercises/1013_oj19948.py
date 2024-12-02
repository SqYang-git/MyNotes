# 脑筋急转弯,(n-1)个间隔,去掉其中(m-1)个,留下(n-m)个最小的
n, m = map(int, input().split())
ranks = list(map(int, input().split()))
ranks.sort()
gap = []
for i in range(len(ranks)-1):
    gap.append(ranks[i+1] - ranks[i])
gap.sort()
ans = sum(gap[:n-m])
print(ans)
