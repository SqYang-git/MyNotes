num = int(input())
count = 0
for i in range(num):
    sum1 = list(map(int, input().split()))
    if sum(sum1) >= 2:
        count += 1

print(count)
