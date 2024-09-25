n = int(input())
a = list(map(int, input().split()))
crime = 0
officers = 0
for i in a:
    if i == -1:
        if officers == 0:
            crime += 1
        else:
            officers -= 1
    if i > 0:
        officers += i
print(crime)
