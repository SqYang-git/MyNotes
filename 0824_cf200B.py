n = int(input())
p = list(map(int, input().split()))

total_orange_juice = sum(p)

average_orange_juice = str(total_orange_juice / n)

print(average_orange_juice)
