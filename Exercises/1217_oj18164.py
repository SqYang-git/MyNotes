import heapq
n = int(input())
rope = list(map(int, input().split()))
heapq.heapify(rope)
ans = 0
for i in range(n-1):
    a = heapq.heappop(rope)
    b = heapq.heappop(rope)
    ans += (a+b)
    heapq.heappush(rope, a+b)
print(ans)
