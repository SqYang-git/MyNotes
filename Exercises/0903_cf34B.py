n, m = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
earn = 0
for i in range(m):
    if lista[i] > 0:
        break
    earn += -lista[i]
print(earn)
