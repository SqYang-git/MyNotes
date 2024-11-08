nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())
    skills = []
    for _ in range(n):
        t, x = map(int, input().split())
        skills.append((t, x))
    skills.sort(key=lambda x: (x[0], -x[1]))
    pre_t = -1
    count = 0
    alive = True
    for t, x in skills:
        if t == pre_t:
            count += 1
        else:
            count = 1
        if count > m:
            continue
        b -= x
        if b <= 0:
            print(t)
            alive = False
            break
        pre_t = t
    if alive:
        print("alive")
