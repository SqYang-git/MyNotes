def minimum(c):
    length = 0
    n = 0
    while length < c:
        n += 1
        length += 1 / (n + 1)
    return n


list1 = []
while True:
    c = float(input())
    if c == 0.00:
        break
    result = minimum(c)
    list1.append(result)

for num in list1:
    print(f"{num:.0f} card(s)")
