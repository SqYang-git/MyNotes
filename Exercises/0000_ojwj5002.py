def hours(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n + hours(n-1) + hours(n-2)


m = int(input())
for i in range(m):
    n = int(input())
    print(hours(n))
