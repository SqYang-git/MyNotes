def solve(stones, count):
    if stones[1]/stones[0] >= 2 or stones[1] % stones[0] == 0:
        if count == 0:
            return "win"
        if count == 1:
            return "lose"
    stones[1] -= stones[0]
    stones.sort()
    count += 1
    count %= 2
    return solve(stones, count)


while True:
    stones = list(map(int,input().split()))
    if stones == [0, 0]:
        exit()
    stones.sort()
    print(solve(stones, 0))
