answers = []


def move(height, start, end, buffer):
    # 如果没有盘子，直接返回
    # 如果有盘子
    if height >= 1:
        # 将上面的盘子从 start 移到 buffer,end作为辅助
        move(height - 1, start, buffer, end)
        # 将最下面的盘子移到 end
        answers.append(f"{start}->{end}")
        # 将 buffer 上的盘子移到 end,start作为辅助
        move(height - 1, buffer, end, start)


n = int(input())
move(n, 'A', 'C', 'B')
print(len(answers))
for ans in answers:
    print(ans)
