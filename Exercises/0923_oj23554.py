n = int(input())
list1 = input().split()

list2 = []
list3 = []
list4 = []

for tag in list1:
    num = int(tag)
    if num > n:
        list3.append(num)
    else:
        list2.append(num)

for i in range(1, n+1):
    if i not in list2:
        list4.append(i)

for in_n in list4:
    print(in_n, end=" ")
print()
for out_of_n in sorted(list3):
    print(out_of_n, end=" ")
