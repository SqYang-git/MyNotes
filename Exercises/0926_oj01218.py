def unlocked(n):
    cells = [0] * n
    for i in range(1, n + 1):
        for j in range(i - 1, n, i):
            cells[j] = 1 - cells[j]
    return sum(cells)


x = int(input())
list1 = []
for i in range(x):
    n = int(input())
    list1.append(unlocked(n))
for num in list1:
    print(num)
