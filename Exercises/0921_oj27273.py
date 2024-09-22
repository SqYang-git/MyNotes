def sum1(n):
    gauss = n * (n + 1) // 2
    position = 1
    sum2 = 0
    while position <= n:
        sum2 += position
        position *= 2
    result = gauss - 2 * sum2
    return result


t = int(input())
results = []
for i in range(t):
    n = int(input())
    result = sum1(n)
    results.append(result)
for result in results:
    print(result)
