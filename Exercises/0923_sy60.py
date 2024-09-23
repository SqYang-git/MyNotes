def is_daffodil(num):
    i = int(num/100)
    j = int(num/10 - 10 * i)
    k = int(num - 100 * i - 10 * j)
    if i ** 3 + j ** 3 + k ** 3 == num:
        return True


couple = input().split()
a = int(couple[0])
b = int(couple[1])
daffodils = []
for m in range(a, b + 1):
    if is_daffodil(m):
        daffodils.append(m)

if len(daffodils) == 0:
    print("NO")
else:
    m = len(daffodils)
    for n in range(m-1):
        print(daffodils[n], end=" ")
    print(daffodils[m-1])
