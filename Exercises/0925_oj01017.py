import math
rest = [0, 5, 3, 1]

while True:
    a, b, c, d, e, f = map(int, input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = d + e + f + math.ceil(c / 4)
    space2 = 5 * d + rest[c % 4]
    if b > space2:
        boxes += math.ceil((b - space2) / 9)
    space1 = 36 * boxes - (36 * f + 25 * e + 16 * d + 9 * c + 4 * b)
    if a > space1:
        boxes += math.ceil((a - space1) / 36)
    print(boxes)
