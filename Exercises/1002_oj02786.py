pell = [0] * (1000000 + 1)
pell[1] = 1
pell[2] = 2
for i in range(3, 1000000 + 1):
    pell[i] = (2 * pell[i - 1] + pell[i - 2]) % 32767


num = int(input())
for _ in range(num):
    j = int(input())
    print(pell[j])
