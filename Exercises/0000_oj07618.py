n = int(input())
list1 = []
list2 = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    if b >= 60:
        list1.append([a, b])
    else:
        list2.append(a)

list1.sort(key=lambda x: x[1], reverse=True)

for i in list1:
    print(i[0])
for i in list2:
    print(i)
