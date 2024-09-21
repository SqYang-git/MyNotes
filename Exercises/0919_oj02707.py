from math import sqrt
n = int(input())
list1 = []
for i in range(n):
    list1.append(list(map(float, input().split())))
for num in list1:
    a, b, c = num[0], num[1], num[2]
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"x1={x1:.5f};x2={x2:.5f}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"x1=x2={x1:.5f}") if b != 0 else print(f"x1=x2=0.00000")
    else:
        re = -b / (2 * a)
        im = sqrt(-delta) / (2 * a)
        if b != 0:
            print(f"x1={re:.5f}+{im:.5f}i;x2={re:.5f}-{im:.5f}i")
        else:
            print(f"x1={0:.5f}+{im:.5f}i;x2={0:.5f}-{im:.5f}i")
