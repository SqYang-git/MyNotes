while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    list1 = [i for i in range(1, n+1)]
    index = 0
    while len(list1) > 1:
        index = (index + m - 1) % len(list1)
        # 注意减1;且一定要在更新list1前更新index,否则index的值错误
        list1.pop(index)
    print(list1[0])
