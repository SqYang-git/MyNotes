is_prime = [True] * 1000001
for i in range(2, int(1000000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1000001, i):
            is_prime[j] = False

def is_t_prime(integer):
    if integer <= 3:
        return False
    root = int(integer ** 0.5)
    if integer == root ** 2:
        return is_prime[root]
    else:
        return False


n = int(input())
list_integers = list(map(int, input().split()))

for i in list_integers:
    if is_t_prime(i):
        print("YES")
    else:
        print("NO")
