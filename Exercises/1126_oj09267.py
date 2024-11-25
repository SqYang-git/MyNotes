N, M = map(int, input().split())
memo = {}


def dfs(step,max_line):
    if max_line >= M:
        return 0
    if step == N:
        return 1
    if (step, max_line) in memo:
        return memo[(step, max_line)]
    ans = (dfs(step+1, 0) + dfs(step+1, max_line+1))
    memo[(step, max_line)] = ans
    return ans


res = dfs(0,0)
print(res)
