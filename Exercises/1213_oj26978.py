from collections import deque
n, k = map(int, input().split())
nums = list(map(int, input().split()))
win = deque(nums[:k])
ans = [max(win)]
count = k
while k < n:
    l = win.popleft()
    r = nums[k]
    win.append(r)
    if l != ans[-1]:
        ans.append(max(ans[-1], r))
    else:
        ans.append(max(win))
    k += 1
print(" ".join(map(str, ans)))
