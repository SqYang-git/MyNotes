weight=int(input())
if weight<4:
    print("No")
if weight>=4:
    if weight % 2 == 0:
        print("Yes")
    else:
        print("No")
