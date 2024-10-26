string = input().lower()
point = 0
count = 1
ans = []
while point <= len(string)-1:
    if point == len(string)-1:
        ans.append(f"({string[point]},{count})")
        break
    elif string[point+1] == string[point]:
        count += 1
        point += 1
    elif string[point+1] != string[point]:
        ans.append(f"({string[point]},{count})")
        point += 1
        count = 1

print("".join(ans))
