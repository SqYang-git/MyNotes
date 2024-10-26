n = int(input())
words = input().split()
ans = []
line = words[0] + " "
for i in words[1:]:
    if len(line + i) <= 80:
        line += i + " "
    else:
        ans.append(line.strip())
        line = i + " "
ans.append(line.strip())
print("\n".join(ans))
