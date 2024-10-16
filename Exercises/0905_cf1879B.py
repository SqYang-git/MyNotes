t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans1 = min(a) * n + sum(b)
    ans2 = min(b) * n + sum(a)
    print(min(ans1, ans2))
