t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    list_num = list(map(int, input().split()))
    buffer = [0] * (n + 1)
    for i in range(1, n + 1):
        buffer[i] = (buffer[i - 1] + list_num[i - 1]) % x
    ans = -1
    left = 0
    right = n
    if buffer[left] != buffer[right]:
        ans = right - left
        print(ans)
        continue
    else:
        num = buffer[left]
        nleft = left; nright = right
        for i in range(left+1, right+1):
            if buffer[i] != num:
                nleft = i
                break
        for j in range(right, left, -1):
            if buffer[j] != num:
                nright = j
                break
        min_step = min(nleft-left, right - nright)
        if min_step == 0:
            print(-1)
            continue
        else:
            ans = right - left - min_step
            print(ans)
            continue
