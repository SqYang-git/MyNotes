import copy


def solve(lights):
    m, n = 5, 6
    # 初始化按按钮矩阵
    pressed = [[0] * n for _ in range(m)]

    def get_light_state(i, j):  # 检查灯泡状态
        if 0 <= i < m and 0 <= j < n:
            return lights[i][j]

    def flip(i, j):  # 翻转灯泡状态
        if 0 <= i < m and 0 <= j < n:
            lights[i][j] ^= 1

    def press(i, j):  # 模拟按压操作
        flip(i, j)
        flip(i - 1, j)
        flip(i + 1, j)
        flip(i, j - 1)
        flip(i, j + 1)

    original_lights = copy.deepcopy(lights)  # 用深拷贝复制嵌套列表

    for num in range(64):   # 遍历第一行初始按压
        lights = copy.deepcopy(original_lights)  # 重置灯状态
        pressed = [[0] * n for _ in range(m)]  # 重置按按钮矩阵
        first_row_press = [0] * n
        buffer = num
        for j in range(n):  # 将num的二进制下位数转换为按压状态
            first_row_press[j] = buffer % 2
            buffer //= 2
        for j in range(n):  # 进行第一行按压
            if first_row_press[j]:
                pressed[0][j] = 1
                press(0, j)
        for i in range(1, m):  # 其余行按题目提示处理
            for j in range(n):
                if get_light_state(i - 1, j) == 1:
                    pressed[i][j] = 1
                    press(i, j)
        if all(get_light_state(m - 1, j) == 0 for j in range(n)):
            result = "\n".join(" ".join(map(str, row)) for row in pressed)
            print(result)
            return


input_lights = []
for _ in range(5):
    input_lights.append(list(map(int, input().split())))
solve(input_lights)
