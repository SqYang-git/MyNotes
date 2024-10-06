def candidates(choices):
    choices.sort(key=lambda x: (x[0], x[1]))
    count = 1
    max_cost_so_far = choices[0][1]
    for i in range(1, len(choices)):
        if choices[i][1] < max_cost_so_far:
            count += 1
            max_cost_so_far = choices[i][1]
    return count


while True:
    n = int(input())
    if n == 0:
        break
    choices = [tuple(map(int, input().split())) for _ in range(n)]
    result = candidates(choices)
    print(result)
