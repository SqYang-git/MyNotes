while "期末要挂QAQ":
    try:
        n = int(input())
        time = list(map(int, input().split()))
        time.sort()
        max_n = time.pop()
        sum_left = sum(time)
        if sum_left < max_n:
            num = sum_left
        else:
            num = (sum_left + max_n) / 2
        print(f"{num:.1f}")
    except EOFError:
        break
