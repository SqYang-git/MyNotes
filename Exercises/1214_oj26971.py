n = int(input())
ratings = list(map(int, input().split()))
candy = [1]*n
for i in range(n-1):
    if ratings[i+1] > ratings[i]:
        candy[i+1] = candy[i] + 1
for i in range(n-1, 0, -1):
    if ratings[i-1] > ratings[i]:
        candy[i-1] = max(candy[i] + 1, candy[i-1])
print(sum(candy))
