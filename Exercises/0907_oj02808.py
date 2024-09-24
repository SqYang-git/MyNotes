def remain(L, M, regions):
    trees = [1] * (L + 1)
    for start, end in regions:
        for i in range(start, end + 1):
            trees[i] = 0
    remaining_trees = sum(trees)
    return remaining_trees


L, M = map(int, input().split())
regions = []
for _ in range(M):
    a, b = map(int, input().split())
    regions.append((a, b))
result = remain(L, M, regions)
print(result)
