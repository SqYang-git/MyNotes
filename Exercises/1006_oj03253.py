while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    list1 = [i for i in range(1, n+1)]
    index = p - 1
    ans = []
    while len(list1) > 1:
        index = (index + m - 1) % len(list1)
        ans.append(list1[index])
        list1.pop(index)
    ans.append(list1[0])
    print(",".join(map(str, ans)))
