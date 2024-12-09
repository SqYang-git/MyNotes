t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if 1 not in arr:
        print(0)
        continue
    max_n = min(arr.count(1), (n+1) // 2)
    arr.remove(1)
    for i in range(1, max_n+1):
        if arr.count(1) == 0:
            print(i)
            break
        arr.remove(1)
        can_use = [x for x in arr if x <= i+1]
        if not can_use:
            print(i)
            break
        else:
            arr.remove(max(can_use))
