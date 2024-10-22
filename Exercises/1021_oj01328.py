num = 0  # 情况编号
while True:
    n, d = map(int, input().split())
    if n == 0:
        break
    else:
        num += 1
        radars = []
        for i in range(n):
            x, y = map(int, input().split())
            if y <= d:
                radars.append(([x - (d ** 2 - y ** 2) ** 0.5, x + (d ** 2 - y ** 2) ** 0.5]))
        input()  # 输入空行
        if len(radars) < n:  # 存在无法覆盖的小岛
            print(f"Case {num}: -1")
        else:
            radars.sort(reverse=True)  # 左端从大到小排序
            count = len(radars)
            i = 0  # 指针(?)
            for j in range(1, n):
                if radars[i][0] > radars[j][1]:  # 无法被前一个覆盖,指针移动,换范围继续判定
                    i = j
                else:  # 可被前一个覆盖
                    count -= 1
            print(f"Case {num}: {count}")
