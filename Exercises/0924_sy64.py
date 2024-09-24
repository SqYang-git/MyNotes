def num_of_couple(lista, k):
    count = 0
    for stra in lista:
        inta = int(stra)
        m = str(k - inta)
        if m in lista:
            count += 1
    return int(count/2)

n = int(input())
lista = input().split()
k = int(input())

print(num_of_couple(lista, k))
