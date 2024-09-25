n = int(input())
print("*")
for i in range(1, n-1):
    print("*", end="")
    for _ in range(i - 1):
        print(" ", end="")
    print("*")
print("*" * n)
