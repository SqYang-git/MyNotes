n, m, a = map(int, input().split())
width = (n + a - 1) // a
height = (m + a - 1) // a
total = width * height
print(total)
