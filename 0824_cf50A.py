def max_dominoes(M, N):
    return (M * N) // 2


M, N = map(int, input().split())
print(max_dominoes(M, N))
