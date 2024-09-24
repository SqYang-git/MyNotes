def how_old_are_you_game(x):
    steps = []
    while x != 1:
        if x % 2 == 0:
            steps.append(f"{x}/2={x // 2}")
            x = x // 2
        else:
            steps.append(f"{x}*3+1={x * 3 + 1}")
            x = x * 3 + 1
    return steps


x = int(input())
steps = how_old_are_you_game(x)
for step in steps:
    print(step)
