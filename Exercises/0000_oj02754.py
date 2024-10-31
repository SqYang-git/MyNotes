# 按顺序存储所有可能的放置方案
answers = []


# 定义递归函数queens
def queens(ans, length):
    for i in range(1, 9):
        # 在同一行,不可放置
        if str(i) in ans:
            continue
        # 在同一斜线,不可放置
        if sum(abs(i - int(ans[j])) == length - j for j in range(length)):
            continue
        else:
            # 若已经完成一个方案
            if length == 7:
                answers.append(ans + str(i))
            # 若未完成方案,加入当前合法位置到ans末尾,继续递归
            else:
                queens(ans + str(i), length + 1)


# 从空字符串开始递归得到所有放置方案
queens("", 0)

n = int(input())
for _ in range(n):
    sequence = int(input()) - 1  # 注意列表编号
    print(answers[sequence])
