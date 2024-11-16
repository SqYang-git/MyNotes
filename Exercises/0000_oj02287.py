while True:
    n = int(input())
    if n == 0:
        break
    TJ = list(map(int, input().split()))
    K = list(map(int, input().split()))
    TJ.sort()
    K.sort()
    profit = 0
    l1 = 0; r1 = n - 1; l2 = 0; r2 = n - 1
    # 未数尽所有马时
    while l1 <= r1:
        # 若目前最弱的马可以赛赢对方目前最弱的马,则用最弱的马赛对方最弱的马.去掉双方最弱的马
        if TJ[l1] >K[l2]:
            profit += 200
            l1 += 1
            l2 += 1
        # 若目前最弱的马不能赛赢目前对方最弱的马
        # 若目前最强的马可以赛赢对方最强的马,比先失利再得利获利更大.
        # 那么应该用最强的马赛对方最强的马.去掉双方最强的马.
        elif TJ[r1] > K[r2]:
            profit += 200
            r1 -= 1
            r2 -= 1
        else:
            # 若最强的马会输给对方最强的马,则用最弱的马赛对方最强的马,充当炮灰.失去200银元.
            if TJ[l1] < K[r2]:
                profit -= 200
            # 若最弱的马与对方最强的马实力相当,仍坚持战术,无需失去银元.
            l1 += 1
            r2 -= 1

    print(profit)
