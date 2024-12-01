n, m, k = map(int, input().split())
steps = set()
board = [[0] * (m+2) for _ in range(n+2)]
for i in range(1, k+1):
    x, y = map(int, input().split())
    if (x, y) in steps:
        continue
    steps.add((x, y))
    board[x][y] = 1
    for j in range(x-1, x+1):
        for k in range(y-1, y+1):
            if board[j][k] == board[j+1][k] == board[j][k+1] == board[j+1][k+1] == 1:
                print(i)
                exit()
print(0)
