n = int(input())
buffer = [0] * ((n+1)//2+1)
for i in range(1, n+1):
    line = [0]+list(map(int, input().split()))
    for j in range(1, n+1):
        k = min(i, j, (n+1)-i, (n+1)-j)
        buffer[k] += line[j]
print(max(buffer))
