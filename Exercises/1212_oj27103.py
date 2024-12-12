N, M = map(int, input().split())
line = list(map(int, input().split()))
count = 1
note = set()
for i in line:
    note.add(i)
    if len(note) == M:
        count += 1
        note.clear()

print(count)
