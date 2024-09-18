count = 0
for i in range(5):
    j = input().find("1")
    if j != -1:
        count += abs(j-4)/2+abs(i-2)

print(f"{count:.0f}")
