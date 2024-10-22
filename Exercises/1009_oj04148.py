num = 1
while True:
    p, e, i, d = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1]:
        break

    count = d+1
    while (count-p) % 23 != 0 or (count-e) % 28 != 0 or (count-i) % 33 != 0:
        count += 1

    print(f"Case {num}: the next triple peak occurs in {count - d} days.")
    num += 1
