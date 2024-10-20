goal = int(input())
lists = list(map(int, input().split()))
lists.sort()

left = 0
right = len(lists) - 1

ans = 200000
gap = 100000 - 2

while left < right:
    sum1 = lists[left] + lists[right]
    if sum1 == goal:
        ans = sum1
        break
    if abs(sum1 - goal) < gap:
        gap = abs(sum1 - goal)
        ans = sum1
    if abs(sum1 - goal) == 0:
        ans = min(ans, sum1)
    if sum1 > goal:
        right -= 1
    elif sum1 < goal:
        left += 1

print(ans)
