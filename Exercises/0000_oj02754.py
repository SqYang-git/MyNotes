ans = []


def q(l, n):
    for i in range(1, 9):
        if not (str(i) in n or sum(abs(i-int(n[j])) == l-j for j in range(l))):
            if l == 7:
                ans.append(n+str(i))
            else:
                q(l+1, n+str(i))


q(0, "")
for _ in range(int(input())):
    print(ans[int(input())-1])
