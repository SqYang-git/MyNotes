import math
q = int(input())
for _ in range(q):
    count = int(input())
    list_num = list(map(int, input().split()))
    buffer = [0] * 12
    try:
        if list_num.index(2048) >= 0:
            print("YES")
            continue
    except ValueError:
        for num in list_num:
            if num < 2048:
                n = int(math.log(num, 2))
                buffer[n] += 1

    for i in range(11):
        if buffer[i] >= 2:
            buffer[i+1] = buffer[i+1] + (buffer[i]//2)
            buffer[i] %= 2

    if buffer[11] != 0:
        print("YES")
    else:
        print("NO")
